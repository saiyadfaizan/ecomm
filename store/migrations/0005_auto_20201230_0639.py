# Generated by Django 2.2.16 on 2020-12-30 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_order_emailaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='email',
        ),
    ]
