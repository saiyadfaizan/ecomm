# Generated by Django 2.2.16 on 2020-12-30 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201230_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='customer',
        ),
    ]
