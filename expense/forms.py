from django import forms
from categories.models import Category
from expense.models import Expense


class QuestionForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        to_field_name='title',
        required=True,  
        widget=forms.Select({'class': 'w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-2'})
    )
    class Meta:
        model = Expense
        fields = ['title','amount','date','category']
