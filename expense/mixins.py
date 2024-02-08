from urllib import request
from django.shortcuts import get_object_or_404
from expense.models import Expense
from django import forms
from categories.models import Category
from django.urls import reverse


class ExpenseListMixin:
    model = Expense
    queryset = Expense.objects.all()

class ExpenseCreateMixin:
    model = Expense
    fields = ['title','amount','date','category']
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'your-class-name'})
    )
    amount = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'your-class-name'})
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'your-class-name'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        to_field_name='title',
        required=True,  
        widget=forms.Select({'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'})
    )

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['category'] = self.category
        form.instance.user = self.request.user
        return form
    
    def get_success_url(self):
        return reverse('expense:list')
    

class ExpenseUpdateMixin:
    model = Expense
    fields = ['title','amount','date','category']
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        to_field_name='title',
        required=True,  
        widget=forms.Select({'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'})
    )
    
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
