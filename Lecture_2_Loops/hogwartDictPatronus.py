# making a list of dictionaries, with 3 options name, house and patronus 
students = [
    {"name":"Hermione", "house": "Gryffindor","patronus": "Otter"},
    {"name":"Harry","house":"Griffindor","patronus":"Stag"},
    {"name":"Ron","house":"Griffindor","patronus":"Jack Russel terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}

]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")



print(students[0])
print(students[1])
print(students[2])
print(students[3])



print(students[0]["name"])
print(students[1]["house"])
print(students[2]["patronus"])


print(students[0]["name"],["house"],["patronus"])


print(students[0]["name"], students[0]["house"],students[0]["patronus"])


for student in students:
    print(student["name"])