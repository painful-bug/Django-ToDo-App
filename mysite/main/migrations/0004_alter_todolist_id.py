# Generated by Django 3.2 on 2021-04-22 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_item_todolist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]