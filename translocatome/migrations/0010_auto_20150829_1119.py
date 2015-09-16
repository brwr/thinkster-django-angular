# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0009_auto_20150829_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='base_activity',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='node',
            name='base_concentration',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='node',
            name='cancer_driver',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='node',
            name='cancer_indirect_driver',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
