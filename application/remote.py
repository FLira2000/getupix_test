from database import initialize_collection

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
				