from django.urls import path
from expense.views import ExpenseListView

app_name = 'expense'
urlpatterns = [
    path('list/', ExpenseListView.as_view(), name='list'),
]
