# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('translocatome', '0004_auto_20150820_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta',
            name='curator_name',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
