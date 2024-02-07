from django.urls import path
from expense.views import ExpenseListView

app_name = 'users'
urlpatterns = [
    path('list/', ExpenseListView.as_view(), name='list'),
]
