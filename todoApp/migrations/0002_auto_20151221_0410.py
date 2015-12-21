# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shards.fields


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='shard_key',
            field=shards.fields.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='todo_list',
            field=shards.fields.ParentKey(to='todoApp.ToDoList'),
        ),
    ]
