# Generated by Django 3.2 on 2022-10-08 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_review_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='status',
        ),
    ]
