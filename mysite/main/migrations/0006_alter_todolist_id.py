# Generated by Django 3.2 on 2021-04-22 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_todolist_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]