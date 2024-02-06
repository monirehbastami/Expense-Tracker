from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from users.forms import UserLoginForm, UserRegisterForm
from .models import User


class UserLoginView(TemplateView):
    form_class = UserLoginForm
    template_name = "user_login.html"
    
    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, "login successful", "success")
                return redirect("users:home")
            else:
                messages.warning(request, "login unsuccessful", "warning")
                return render(request, self.template_name, {"form" : form})
            

class UserRegisterView(TemplateView):
    template_name = "user_register_form.html"
    form_class = UserRegisterForm
    def get(self,request,*args,**kwargs):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = User.objects.create(username=form.cleaned_data['username'],\
            email=form.cleaned_data['email'],phone_number=form.cleaned_data\
            ['phone_number'],national_id=form.cleaned_data['national_id'])
            obj.set_password(form.cleaned_data["password"])
            obj.save()
            messages.success(request,'You register successfully')
            return redirect("users:login")
   