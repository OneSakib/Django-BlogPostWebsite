from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, BlogComment
from django.contrib import messages
from blog.templatetags import extras


# Create your views here.
def bloghome(request):
    allPost = Blog.objects.all()
    params = {'allPost': allPost}
    return render(request, 'blog/home.html', params)
    # return HttpResponse("Home page of Blog")


def blogPost(request, slug):
    post = Blog.objects.get(slug=slug)
    print(post.views)
    post.views += 1
    post.save()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    params = {'post': post, 'comments': comments[::-1], 'user': request.user, 'replyDict': replyDict}
    return render(request, 'blog/blogpost.html', params)
    # return HttpResponse(f"Blog Page : {slug}")


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        parentSno = request.POST.get('parentSno')
        post = Blog.objects.get(sno=postSno)
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
        comment.save()
        messages.success(request, " Your Comment has been posted successfuly ")
        return redirect(f'/blog/{post.slug}')

    else:
        messages.error(request, " Some Error Issue Found Not Comment is not send")
        return redirect('/')
