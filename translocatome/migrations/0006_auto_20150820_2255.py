# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0005_auto_20150820_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effectvalue',
            name='value',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meta',
            name='data_source',
            field=models.ManyToManyField(to='translocatome.DataSource', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meta',
            name='references',
            field=models.ManyToManyField(to='translocatome.Reference', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meta',
            name='reviewed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
