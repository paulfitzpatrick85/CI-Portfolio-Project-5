# Generated by Django 3.2 on 2022-10-05 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_remove_reviews_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
