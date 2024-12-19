import json


some_dict = {
    "name": "Alice",
    20: "was int",
    "age": 25,
    "is_student": False,
    "None_value": None,
    "float_value": 2.222,
    "skills": ["Python", "Data Analysis"]
}

# with open("json_file.json", "w") as f:
#     json.dump(some_dict, f, indent=2)
#
# with open("json_file.json", "r") as f:
#     my_dict = json.load(f)
#     print(my_dict)

# ----- пример форматирования -------

json_representation = json.dumps(some_dict, indent=2)

print(json.loads(json_representation))