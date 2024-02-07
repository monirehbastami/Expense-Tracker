from django.db import models
from categories.models import Category
from users.models import User

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()
    category = models.ManyToManyField(Category, related_name='cat_exp')
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)


