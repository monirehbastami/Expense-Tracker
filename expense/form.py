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
            'date': forms.DateInput(attrs={'type': 'date','class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}),
            'category': forms.Select(attrs={'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'})
        }
        

class FilterForm(forms.Form):
    date1 = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date','class': 'w-42 px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}), required=False)
    date2 = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date','class': 'w-42 px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}), required=False)
    amount1 = forms.FloatField(label='Min Price',widget=forms.TextInput(attrs={'class': 'w-32 px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}), required=False,min_value=0)
    amount2 = forms.FloatField(label='max Price',widget=forms.TextInput(attrs={'class': 'w-32 px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}), required=False,min_value=0)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='---', widget=forms.Select(attrs={'class': 'w-42 px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'}), required=False)
            
