from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class ExpensesList(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Item(models.Model):
    expenseslist = models.ForeignKey(ExpensesList, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    price = models.FloatField()


    def __str__(self):
        return self.item_name
