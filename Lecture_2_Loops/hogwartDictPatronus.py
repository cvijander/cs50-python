# making a list of dictionaries, with 3 options name, house and patronus 
students = [
    {"name":"Hermione", "house": "Gryffindor","patronus": "Otter"},
    {"name":"Harry","house":"Griffindor","patronus":"Stag"},
    {"name":"Ron","house":"Griffindor","patronus":"Jack Russel terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}

]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")