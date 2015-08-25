# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BiologicalProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.SmallIntegerField(choices=[(0, b'apoptosis'), (1, b'cri'), (2, b'ddr'), (3, b'hypoxia'), (4, b'mapk'), (5, b'plc'), (6, b'prolif')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.SmallIntegerField(choices=[(0, b'base_ppi'), (1, b'manual_curation'), (2, b'signaling_pool')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeneName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edge_type', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('directness', models.PositiveSmallIntegerField(choices=[(0, b'direct'), (1, b'indirect'), (2, b'unknown'), (3, b'direct_and_indirect')])),
                ('effect_all', models.PositiveSmallIntegerField(choices=[(2, b'negative'), (1, b'neutral'), (0, b'positive'), (3, b'both'), (4, b'unknown'), (5, b'minimal_positive'), (6, b'minimal_negative')])),
                ('effect_final', models.PositiveSmallIntegerField(choices=[(2, b'negative'), (1, b'neutral'), (0, b'positive'), (3, b'both'), (4, b'unknown'), (5, b'minimal_positive'), (6, b'minimal_negative')])),
                ('score', models.SmallIntegerField(choices=[(0, b'zero'), (1, b'one'), (2, b'two'), (3, b'unknown'), (4, b'not_applicable')])),
                ('int_abrev', models.CharField(max_length=13)),
                ('is_in_full', models.BooleanField(default=False)),
                ('is_in_medium', models.BooleanField(default=False)),
                ('is_in_small', models.BooleanField(default=False)),
                ('is_in_skeleton', models.BooleanField(default=False)),
                ('biological_process', models.ManyToManyField(to='translocatome.BiologicalProcess')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InteractionSubtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InteractionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=50)),
                ('subtype', models.ManyToManyField(to='translocatome.InteractionSubtype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=500)),
                ('entry_state', models.SmallIntegerField(choices=[(0, b'integrated'), (1, b'manually_rewired'), (2, b'deleted'), (3, b'rewired')])),
                ('reviewed', models.BinaryField()),
                ('curators_comment', models.CharField(max_length=500)),
                ('curator_name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('data_source', models.ManyToManyField(to='translocatome.DataSource')),
                ('interaction', models.ForeignKey(to='translocatome.Interaction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene_name', models.ForeignKey(to='translocatome.GeneName')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference_type', models.SmallIntegerField(choices=[(0, b'pubmed'), (1, b'book'), (2, b'manual')])),
                ('value', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UniProtAc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='node',
            name='uni_prot_ac',
            field=models.ForeignKey(to='translocatome.UniProtAc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meta',
            name='references',
            field=models.ManyToManyField(to='translocatome.Reference'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meta',
            name='sources',
            field=models.ManyToManyField(to='translocatome.Source'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interaction',
            name='interaction_type',
            field=models.ManyToManyField(to='translocatome.InteractionType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interaction',
            name='source_node',
            field=models.ForeignKey(related_name='source', to='translocatome.Node'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='interaction',
            name='target_node',
            field=models.ForeignKey(related_name='target', to='translocatome.Node'),
            preserve_default=True,
        ),
    ]
