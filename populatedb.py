import subprocess
import random
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#exportStatement = 'DJANGO_SETTINGS_MODULE='+os.path.join(BASE_DIR,'demo/settings.py')
#subprocess.call(['export ', exportStatement], shell=True)
path = os.path.join(BASE_DIR,'demo/settings.py')
print path
os.environ['DJANGO_SETTINGS_MODULE'] = path
print os.environ['DJANGO_SETTINGS_MODULE']

#sys.path.append('todoApp/')
 
from todoApp.models import ToDoList, ToDoItem

NUM_THINGS = 1000

words = open('wordlist.txt','r')
tot_count=0
while (tot_count < NUM_THINGS):

	list_title = words.readline()
	_list = ToDoList()
	_list.title = list_title
	_list.save()
	list_id = _list.id

	num_items = int(random.random()*25+1)
	for i in range(num_items):
		item_title = words.readline()
		item = ToDoItem()
		item.title = item_title
		item.completed = True if (i%2==1) else False
		item.todo_list = list(ToDoList.objects.all().filter(id=list_id))[0]
		item.save()

	tot_count+=num_items+1

