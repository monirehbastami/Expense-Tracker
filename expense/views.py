from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from expense.mixins import ExpenseListMixin

decorators = [never_cache, login_required(login_url='users:home')]


@method_decorator(decorators, name="dispatch")
class ExpenseListView(ExpenseListMixin,ListView):
    template_name = 'expense_list_view.html'
    
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context ={
            'expenses':self.get_queryset()
        }
        return self.render_to_response(context)
