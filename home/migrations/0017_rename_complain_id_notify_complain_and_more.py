# Generated by Django 4.0.6 on 2022-07-22 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_unit_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notify',
            old_name='complain_id',
            new_name='complain',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='complain_by',
        ),
        migrations.AddField(
            model_name='notify',
            name='assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.employee', verbose_name='assigned to'),
        ),
        migrations.AddField(
            model_name='notify',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='home.tenant', verbose_name='complain by'),
            preserve_default=False,
        ),
    ]
