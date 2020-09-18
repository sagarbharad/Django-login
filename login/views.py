from django.shortcuts import render
import secrets
from django.contrib.auth import logout
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password, make_password
from .models import Client
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    email=request.session['email']
    user=Client().get_user_by_email(email)
    data={}
    data['user']=user

    return render(request,"profile.html", data)


def login(request):
    error_message=""
    email = request.POST.get('email')
    password = request.POST.get('password')
    user=Client().get_user_by_email(email)
    if request.POST:
        if user:
            flag = check_password(password, user.password)
            if flag:
                request.session['email'] = email
                return redirect("/profile")
            else:
                error_message = 'Password invalied !!'
        else:
            error_message = "Email Not Registered Kindly Register"
    data = {}
    data['error'] = error_message
    return render(request,"login.html", data)

def signup(request):
    error=""
    if request.POST:
        if request.POST.get('password')== request.POST.get('confirm_password'):
            client=Client()
            client.first_name=request.POST.get('first_name')
            client.last_name=request.POST.get('last_name')
            client.age=request.POST.get('age')
            unique=request.POST.get('unique')
            if unique.isalnum():
                client.unique=unique
            else:
                client.unique= secrets.token_hex(3)
            client.email=request.POST.get('email')
            client.password = make_password(request.POST.get('password'))
            image1 = request.FILES.get('image')
            c_image1=None
            if image1:
                file_name = FileSystemStorage().save(image1.name, image1)
                c_image1 = FileSystemStorage().url(file_name)
                c_image1 = image1.name
                client.image = c_image1
            client.save()
            error_message="SignUp Successfull! You Can Login Now!"
            data = {}
            data['error'] = error_message
            return render(request,"login.html", data)
        else:
            error="Confirm Password Not Same"
    data={}
    data['error']=error
    return render(request,"signup.html", data)

def logout_user(request):
    logout(request)
    error_message="LoginNow"
    return redirect("/login")
