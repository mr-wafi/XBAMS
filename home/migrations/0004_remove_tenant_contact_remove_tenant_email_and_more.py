# Generated by Django 4.0.3 on 2022-06-30 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_tenant_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='email',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='password',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='tenant_name',
        ),
    ]
