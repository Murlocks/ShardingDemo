from django.db import models
from shards.models import ShardableModel
from shards.fields import BigIntegerField, ParentKey
import datetime


# Create your models here.
class ToDoList(ShardableModel):
    shard_group = 'shard_group_one'
    shard_key = BigIntegerField(sharding_root=True)

    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class ToDoItem(ShardableModel):
    shard_group = 'shard_group_one'
    title = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    completed = models.BooleanField(default=False)
    # todo_list = models.ForeignKey(ToDoList)
    todo_list = ParentKey(ToDoList)

    def __str__(self):
        return self.title
