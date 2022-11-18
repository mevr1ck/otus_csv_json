import csv
import json
import time

from files import BOOKS_FILE, USERS_FILE

result_file = "result.json"

USER_ATTRS = ('name', 'gender', 'address', 'age', 'books')
BOOK_ATTRS = ('title', 'author', 'pages', 'genre')


def get_result():
	with open(BOOKS_FILE, 'r') as csv_file:
		books = list(csv.DictReader(csv_file))
		for i in books:
			del i['Publisher']
	
	with open(USERS_FILE, 'r') as json_file:
		result_file = []
		for i in json.load(json_file):
			result_file.append(
				{'name': i.get('name'),
				 'gender': i.get('gender'),
				 'address': i.get('address'),
				 'age': i.get('age'),
				 'books': []})
	
	while len(books) > 0:
		for i_user in result_file:
			if len(books) > 0:
				i_user['books'].append(books.pop())
	
	with open('result.json', 'w') as r:
		result = json.dumps(result_file, indent=4)
		r.write(result)


get_result()
