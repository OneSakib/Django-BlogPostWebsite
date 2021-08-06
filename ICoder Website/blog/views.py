from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def bloghome(request):
    return render(request, 'blog/home.html')
    # return HttpResponse("Home page og Blog")


def blogPost(request, slug):
    return render(request, 'blog/blog.html' )
    # return HttpResponse(f"Blog Page : {slug}")
