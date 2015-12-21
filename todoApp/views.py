from django.shortcuts import render_to_response

from todoApp.models import ToDoList


def status(request):
    todoLists = []
    for shard_key in [1, 2]:
        for _list in ToDoList.objects.all(shard_key=shard_key):
            todo_dict = {}
            todo_dict['list_object'] = _list
            todo_dict['item_count'] = _list.todoitem_set.count()
            todo_dict['items_complete'] = _list.todoitem_set.filter(shard_key=shard_key, completed=True).count()
            todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)
            todoLists.append(todo_dict)

    return render_to_response('status.html', {'todo_listing': todoLists})
