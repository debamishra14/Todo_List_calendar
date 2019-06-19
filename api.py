import requests
import json


BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

def get_todos(id=None):
	data={}

	if id is not None:
		data={
			'id':id
		}
	resp = requests.get(BASE_URL+ENDPOINT, data=json.dumps(data))
	# print(resp.status_code)
	print(resp.json())

# get_todos('27')     # uncomment to get lists based on id's of list
get_todos()			  # This is to get all list 
