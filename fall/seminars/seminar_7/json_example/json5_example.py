import pyjson5

# строки будут игнорироваться
with open("json_commented.json", "r") as f:
    data = pyjson5.load(f)

print(data)