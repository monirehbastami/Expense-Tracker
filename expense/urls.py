from django.urls import path
from expense.views import ExpenseCreateView, ExpenseListView, ExpenseUpdateView

app_name = 'expense'
urlpatterns = [
    path('list/', ExpenseListView.as_view(), name='list'),
    path('create/', ExpenseCreateView.as_view(),name='create'),
    path('update/<int:pk>/',ExpenseUpdateView.as_view(),name='update')
]
