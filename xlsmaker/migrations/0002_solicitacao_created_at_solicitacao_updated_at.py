# Generated by Django 5.1.7 on 2025-03-25 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlsmaker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
