# Generated by Django 4.0.3 on 2022-07-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_notify_complain_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='status',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
