# Generated by Django 3.2 on 2022-11-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_rename_order_orderlineitem_package_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='package_ordered',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='package_ordered',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]