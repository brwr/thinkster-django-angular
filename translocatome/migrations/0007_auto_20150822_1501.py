# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('translocatome', '0006_auto_20150820_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=500)),
                ('entry_state', models.SmallIntegerField(choices=[(0, b'integrated'), (1, b'manually_rewired'), (2, b'deleted'), (3, b'rewired')])),
                ('reviewed', models.BooleanField(default=False)),
                ('curators_comment', models.CharField(max_length=500)),
                ('curator_name', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('data_source', models.ManyToManyField(to='translocatome.DataSource', null=True)),
                ('interaction', models.ForeignKey(to='translocatome.Interaction')),
                ('references', models.ManyToManyField(to='translocatome.Reference', null=True)),
                ('sources', models.ManyToManyField(to='translocatome.Source')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='meta',
            name='curator_name',
        ),
        migrations.RemoveField(
            model_name='meta',
            name='data_source',
        ),
        migrations.RemoveField(
            model_name='meta',
            name='interaction',
        ),
        migrations.RemoveField(
            model_name='meta',
            name='references',
        ),
        migrations.RemoveField(
            model_name='meta',
            name='sources',
        ),
        migrations.DeleteModel(
            name='Meta',
        ),
        migrations.AlterField(
            model_name='node',
            name='gene_name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='node',
            name='uni_prot_ac',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='node',
            unique_together=set([('uni_prot_ac', 'gene_name')]),
        ),
    ]
