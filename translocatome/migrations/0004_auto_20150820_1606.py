# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0003_auto_20150820_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='score',
            field=models.SmallIntegerField(null=True),
            preserve_default=True,
        ),
    ]
