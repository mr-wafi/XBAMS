# Generated by Django 4.0.6 on 2022-07-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_visitor_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='image',
            field=models.ImageField(upload_to='tenant/'),
        ),
    ]
