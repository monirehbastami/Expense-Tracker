from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,UpdateView
from expense.mixins import ExpenseListMixin, ExpenseCreateMixin, ExpenseUpdateMixin

decorators = [never_cache, login_required(login_url='users:home')]


@method_decorator(decorators, name="dispatch")
class ExpenseListView(ExpenseListMixin,ListView):
    template_name = 'expense_list_view.html'
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context ={
            'expenses':self.get_queryset()
        }
        return self.render_to_response(context)


@method_decorator(decorators, name="dispatch")
class ExpenseCreateView(ExpenseCreateMixin,CreateView):
    template_name = 'expense_form.html' 


@method_decorator(decorators, name="dispatch")
class ExpenseUpdateView(ExpenseUpdateMixin,UpdateView):
    template_name = 'expense_form.html'