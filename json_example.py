import json


json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data =  json.loads(json_data)
print(parsed_data, type(parsed_data))


data = {
    "name": "Иван",
    "age": 30,
    "is_student": False
}
json_string = json.dumps(data)
print(json_string)