
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import *
import datetime
import uuid

# Create your views here.
# def index(request):
#     now = datetime.datetime.now()
#     current_hour = now.hour

#     if current_hour < 12:
#         greeting = "Good morning"
#     elif 12 <= current_hour < 18:
#         greeting = "Good afternoon"
#     else:
#         greeting = "Good evening"
#     context = {'greeting':greeting,'mydate':now, }
    
#     if request.method == 'POST':
#         username = request.POST['name']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password = password)

#         if user is not None:
#             auth.login(request, user)
#             return render(request, 'homepage.html')
#             # return redirect('homepage')
#         else:
#             messages.info(request, "Invalid credentials")
#             return redirect('/')
#     return render(request, 'index.html',context)


def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'accounts/homepage.html')
        else:
            messages.info(request, "Wrong username and Password")
            return redirect('/')
    
    return render(request, 'accounts/signin.html')


@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    now = datetime.datetime.now()
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        username = firstname +' '+lastname 
        
        #gender = request.POST['gender']
        # btown = request.POST['btown']
        # bday = request.POST['bday']
        # htown = request.POST['htown']
        # street = request.POST['street']
        # skill = request.POST['class']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username Taken")
                return redirect('/register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
                user.save()
                profile = UsersDetail.objects.create(Name=username, email=email, start_date=now.strftime("%Y-%m-%d"))
                #profile = Profile.objects.create(Name=username, Gender=gender, email=email, Birthtown= btown, birth_date= bday, Street= street, Hometown=htown, Class= skill, position = "student", start_date=now.strftime("%Y-%m-%d"))
                profile.save()
                return redirect('/')
           
        elif password != cpassword:
            messages.info(request, "Password Mismatch")
            return redirect('register')
        
    return render(request, 'accounts/signup.html') 


@login_required(login_url='/')
def homepage(request):
    user = User.objects.get(username=request.user.username)
    context = {"user": user}
    return render(request, 'accounts/homepage.html')

