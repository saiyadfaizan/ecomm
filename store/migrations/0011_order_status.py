# Generated by Django 2.2.16 on 2021-01-08 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PD', 'Pending'), ('DR', 'Delivered')], default='PD', max_length=2),
        ),
    ]