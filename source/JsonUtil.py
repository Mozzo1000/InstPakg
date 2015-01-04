import json

data = None
json_data = None

def load_json(json_file):
	global data
	global json_data
	json_data = open(json_file)
	data = json.load(json_data)

def get_json(value):
	return data[value]

def close_json():
	json_data.close()
	
