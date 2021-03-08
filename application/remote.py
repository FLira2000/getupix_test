from database import initialize_collection
from datetime import date

collection = initialize_collection()

def find_one(data):
    return collection.find_one(data) or {}

def find_various(data):
    pass

def insert_one(data):
    collection.insert_one(data)

def insert_multiple(data):
    pass

def alter(data):
    pass

def delete(data):
    return collection.delete_one(data)

def find_population(population):
	cursor = collection.find()

	# eu nao irei fazer um list comprehension aqui pq senão ficaria horrivel de ler
	for doc in cursor:
		for x in doc['population']:
			if float(doc['population'][str(x)]) == float(population):
				return doc
				
def find_custom(dict_data):
	cursor = collection.find({'location': dict_data['location']})
	quant_doc = 0
	for doc in cursor:
		for x in doc['iso_code']:
			if doc['iso_code'][x] == dict_data['iso_code']:
				print(doc['iso_code'])
				for p in doc['date']:
					if date.fromisoformat(doc['date'][p]) > date.fromisoformat(dict_data['date']):
						print(doc['date'])
						quant_doc+=1
						break
	return quant_doc