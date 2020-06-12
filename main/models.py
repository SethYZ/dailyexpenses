from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExpensesList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    expenseslist = models.ForeignKey(ExpensesList, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    price = models.FloatField()


    def __str__(self):
        return self.item_name
