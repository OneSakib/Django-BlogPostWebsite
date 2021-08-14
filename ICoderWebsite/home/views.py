from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
from blog.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    allBlogs = Blog.objects.all()
    params = {'allBlogs': allBlogs}
    return render(request, 'home/home.html', params)
    # return HttpResponse("Home of Home");


def about(request):
    return render(request, 'home/about.html')
    # return HttpResponse("About of Home");


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) != 0 or len(email) != 0 or len(phone) != 0 or len(content) != 0:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, " Your Details is Successfuly Save")
        else:
            messages.error(request, " Please Fill the Right Details")

    return render(request, 'home/contact.html')
    # return HttpResponse("Contact of Home");


def search(request):
    if request.method == "GET":
        query = request.GET['search']
        if len(query) > 78:
            allPost = []
            messages.error(request, " Please Fill the search to Short text this is very long")
        if len(query) < 2:
            allPost = []
            messages.error(request, " Please Fill the search Some text")
        else:
            allPost = Blog.objects.filter(title__icontains=query)
            if len(allPost) < 1:
                messages.error(request, " No Search results is Found please write related text")
            else:
                messages.success(request, " Results Successfuly get down")

        params = {'allPost': allPost}
    return render(request, 'home/search.html', params)
    # return HttpResponse("Search Results")


def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Check errorneous inputs
        # User Nmae Must be les than 10 Characters
        if len(username) > 10 or len(username) < 1:
            messages.error(request, "User Name Must Be less than 10 Characters ")
            return redirect('/')

        # User Name Must be Characters
        if not username.isalnum():
            messages.error(request, "User Name Shourld Only Contain Alphabets Not any Other Number or Sybmols")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, "Password Don't Match")
            return redirect('/')

        # Create the User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your ICode Ac has been successfuly Sign Up")
        print(username, fname, lname, email, pass1, pass2)
        return redirect('/')
    else:
        messages.error(request, " Some Error Found! Please Correct Details Entered ")
        return redirect('/')


def handlelogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, " Your Successful login")
            return redirect('/')
        else:
            messages.error(request, " Check your username and Password")
            return redirect('/')
    else:
        messages.error(request, " Check your username and Password")
        return redirect('/')


def handlelogout(request):
    logout(request)
    messages.success(request, " You are Successfuly logout")
    return redirect('/')
