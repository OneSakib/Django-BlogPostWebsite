from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home/home.html')
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
