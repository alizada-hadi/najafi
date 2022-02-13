from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register_view(request):
   if request.method == "POST":
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request, 'your account created successfully !!')
         return redirect("register")
   else:
      form = UserRegisterForm()
      messages.warning(request, 'your account not created!!')
   context = {
      "form" : form
   }   

   return render(request, "accounts/register.html",  context)

   
def login_view(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username = username, password = password)
      if user is not None:
         login(request, user)
         return redirect('product')
      else:
         messages.warning(request, 'your password and username is incorret')
   
   return render(request, 'accounts/login.html')

def logout_view(request):
   logout(request)
   return redirect('login')