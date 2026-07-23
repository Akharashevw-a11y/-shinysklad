import json

with open("data.json", "r") as file:
    data = json.load(file)

print("Данные проекта:")
print(data)
