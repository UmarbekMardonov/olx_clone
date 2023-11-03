# Generated by Django 4.2.6 on 2023-11-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxapp', '0007_alter_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='adds',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='adds',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
