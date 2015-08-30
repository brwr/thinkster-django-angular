# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0011_auto_20150829_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='base_activity',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='node',
            name='base_concentration',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='node',
            name='cancer_driver',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='node',
            name='cancer_indirect_driver',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
