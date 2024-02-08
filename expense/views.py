import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,UpdateView
from expense.form import FilterForm
from expense.mixins import ExpenseListMixin, ExpenseCreateMixin, ExpenseUpdateMixin
from django.utils.dateparse import parse_date


decorators = [never_cache, login_required(login_url='users:home')]


@method_decorator(decorators, name="dispatch")
class ExpenseListView(ExpenseListMixin,ListView):
    template_name = 'expense_list_view.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        date1 = self.request.POST.get('date1')
        date2 = self.request.POST.get('date2')
        amount1 = self.request.POST.get('amount1')
        amount2 = self.request.POST.get('amount2')
        category = self.request.POST.get('category')
        filters = {'user': self.request.user}
        if date1:
            filters['date__gte'] = date1
        if date2:
            filters['date__lte'] = date2
        if amount1:
            filters['amount__gte'] = amount1
        if amount2:
            filters['amount__lte'] = amount2
        if category:
            filters['category'] = category
        if filters:
            return queryset.filter(**filters)
        else:
            return queryset.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        form = FilterForm()
        context = {
            'form': form,
            'expenses': self.get_queryset()
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = FilterForm(request.POST)
        if form.is_valid():
            self.object_list = self.get_queryset()
        context = {
            'form': form,
            'expenses': self.object_list
        }
        return render(request, self.template_name, context) 
    
@method_decorator(decorators, name="dispatch")
class ExpenseCreateView(ExpenseCreateMixin,CreateView):
    template_name = 'expense_form.html' 


@method_decorator(decorators, name="dispatch")
class ExpenseUpdateView(ExpenseUpdateMixin,UpdateView):
    template_name = 'expense_form.html'