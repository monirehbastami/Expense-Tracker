from django.views.generic import ListView
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from expense.mixins import ExpenseListMixin
from users.charts import create_expense_chart
from users.forms import UserLoginForm, UserRegisterForm
from .models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from matplotlib import pyplot as plt
from expense.models import Expense
import io
import urllib,base64

decorators = [never_cache, login_required(login_url='users:home')]


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
                return redirect("users:dashboard")
            else:
                messages.warning(request, "login unsuccessful", "warning")
                return render(request, self.template_name, {"form" : form})
        return render(request, self.template_name, {'form': form})   


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
            return redirect("users:home")
        return render(request, self.template_name, {'form': form})


@method_decorator(decorators, name="dispatch")
class UserHomeView(ExpenseListMixin,ListView):
    template_name = "user_home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expenses = Expense.objects.filter(user=self.request.user)
        categories = [expense.category.title for expense in expenses]
        amounts = [expense.amount for expense in expenses]
        fig, ax = plt.subplots()
        ax.bar(categories, amounts)
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read()).decode('utf-8')
        uri = urllib.parse.quote(string)
        context['data1'] = uri

        

        return context
    
class UserLogoutView(TemplateView):
    def get(self,request):
        logout(request)
        return redirect('users:home')