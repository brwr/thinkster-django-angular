# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0012_auto_20150829_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='edge_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 1), (1, 2), (2, 3), (3, 4)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interactionsubtype',
            name='value',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='interactiontype',
            name='value',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
