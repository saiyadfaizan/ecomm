# Generated by Django 2.2.16 on 2020-12-30 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_emailaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='emailAddress',
        ),
    ]