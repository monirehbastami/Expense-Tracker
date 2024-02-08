from django.db import models
from categories.models import Category
from users.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField(validators=[MinValueValidator(0)])
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)


