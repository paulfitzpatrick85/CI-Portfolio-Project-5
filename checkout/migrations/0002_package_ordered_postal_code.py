# Generated by Django 3.2 on 2022-11-13 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package_ordered',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]