# Generated by Django 4.2.2 on 2023-07-20 03:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='memo_posted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='memo_text',
            field=models.TextField(default=''),
        ),
    ]