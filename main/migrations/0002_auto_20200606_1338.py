# Generated by Django 3.0.5 on 2020-06-06 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expenses',
            new_name='ExpensesList',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('expenseslist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ExpensesList')),
            ],
        ),
    ]
