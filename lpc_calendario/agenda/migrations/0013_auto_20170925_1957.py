# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 22:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agenda', '0012_auto_20170918_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendainstitucional',
            name='feriados',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='compromissos',
        ),
        migrations.RemoveField(
            model_name='agenda',
            name='usuarios',
        ),
        migrations.RemoveField(
            model_name='compromisso',
            name='data',
        ),
        migrations.AddField(
            model_name='agenda',
            name='institucional',
            field=models.BooleanField(default=1, verbose_name=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agenda',
            name='usuario',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agenda',
            name='visivel',
            field=models.BooleanField(default=1, verbose_name=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compromisso',
            name='agendas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Agenda'),
        ),
        migrations.AddField(
            model_name='compromisso',
            name='dataHoraFim',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compromisso',
            name='dataHoraInicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='AgendaInstitucional',
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
