# Generated by Django 4.0.3 on 2022-07-02 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_notify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.employee'),
        ),
        migrations.AlterField(
            model_name='notify',
            name='complain_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.complain'),
        ),
    ]
