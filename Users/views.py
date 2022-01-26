import os
import random
import requests

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect


# Create your views here.
OTP = random.randint(1000,9999)
SMS_API = os.getenv('SMS_API')

def signup(request):
    if request.method=='POST':
        if request.POST.get('password') == request.POST.get('password2'):
            try:
                User.objects.get(username  = request.POST.get('mobile'))
                return render(request, 'users/signup.html',{'error':'Mobile number already Used by someone.'})
            except User.DoesNotExist:
                mobile = request.POST.get('mobile')
                # password = 
                user = User.objects.create_user(mobile, password=request.POST.get('password'))
                user.is_active = False
                user.save()
                # auth.login(request, user)
                # mobile = re
                url = "https://www.fast2sms.com/dev/bulkV2"
                data = f"sender_id=TXTIND&message= Your One-Time_Password is : \n {OTP}&route=v3&language=hindi&numbers={mobile}"
                headers = {
                    'authorization': SMS_API,
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                    }
                response = requests.request("POST",
                                          url,
                                          data=data, 
                                          headers=headers)
                print(response.text)
                return redirect('users:verify', id=mobile)
        else:
            return render(request, 'users/signup.html',{'error':'Please enter same password.'})
    else:
        return render(request, 'users/signup.html')

def login(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST.get('mobile'), password=request.POST.get('password'))
        if user is not None:
            auth.login(request, user)
            if request.POST.get('next'):
              return HttpResponseRedirect(request.POST.get('next'))
            else:
              return redirect('moneyfi:moneyfi')
        else:
            return render(request, 'users/login.html',{'error':"Please enter correct mobile number and password"})
    else:
        return render(request, 'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect('works')

# @loagou
def verify(request, id):
  print(id)
  if request.method=='POST':
    if int(request.POST.get('otp'))==OTP:
      user = User.objects.filter(username = id)[0]
      user.is_active = True
      user.save()
      return redirect('users:login')
    else:
      return render(request, 'users/verify.html', {'error':'Please enter correct OTP.'})

  else:
    return render(request, 'users/verify.html')

