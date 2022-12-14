import json

db = {
    '1982143703': {'ISBN': '1982143703', 'title': 'In Five Years', 'author': 'Rebecca Serle', 'genre': 0, 'publishYear': 2020},
    '1938120752': {'ISBN': '1938120752', 'title': 'Turning the Pyramid Upside Down', 'author': 'Marilyn D. Jacobson', 'genre': 4, 'publishYear': 2013}}

with open("service\database.json", "w+") as f:
    json.dump(db, f)