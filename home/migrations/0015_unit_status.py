# Generated by Django 4.0.6 on 2022-07-17 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_tenant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='status',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
