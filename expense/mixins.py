from urllib import request
from django.shortcuts import get_object_or_404
from expense.models import Expense
from django import forms
from categories.models import Category
from django.urls import reverse
from .form import ExpenseCreateForm

class ExpenseListMixin:
    model = Expense
    queryset = Expense.objects.all()

class ExpenseCreateMixin:
    model = Expense
    form_class = ExpenseCreateForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance.user = self.request.user
        return form
    
    def get_success_url(self):
        return reverse('expense:list')
    

class ExpenseUpdateMixin:
    model = Expense
    form_class = ExpenseCreateForm
    
    def get_object(self, queryset=None):
        return get_object_or_404(Expense, pk=self.kwargs['pk'], user=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.initial['category'] = self.get_object().category
        form.instance.user = self.request.user
        return form
    
    def get_success_url(self):
        return reverse('expense:list')
    


class ExpenseDetailMixin:
    model = Expense
    pk_url_kwarg = "pk"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Expense = self.get_object()
        context['category'] = Expense.category.title
        return context
