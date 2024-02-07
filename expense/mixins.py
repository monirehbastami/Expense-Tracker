from expense.models import Expense

class ExpenseListMixin:
    model = Expense
    queryset = Expense.objects.all()