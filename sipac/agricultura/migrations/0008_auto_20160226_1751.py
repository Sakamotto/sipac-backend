# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-26 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agricultura', '0007_auto_20160224_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producao',
            name='area_colhida',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='producao',
            name='area_em_formacao',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='producao',
            name='area_plantada',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='producao',
            name='irrigado',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='producao',
            name='producao',
            field=models.IntegerField(null=True),
        ),
    ]