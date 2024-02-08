from django import forms
from .models import Expense
from categories.models import Category

class ExpenseCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='---', widget=forms.Select(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}))
    class Meta:
        model = Expense
        fields = ['title','amount','date','category']
        

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}),
            'date': forms.DateInput(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}),
            'category': forms.Select(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'})
        }
        