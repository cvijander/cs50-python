#students = ["Hermione","Harry", "Ron","Draco"]
#houses = ["Griffindor","Griffindor", "Griffindor","Slytherin"]


emptyDictionary = {}


students = {
    "Hermione": "Griffindor",
    "Harry" : "Griffindor",
    "Ron" : "Griffindor",
    "Draco" : "Slytherin"
}

# trazenje vrednosti rucno 
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


# trazenje vrednosti preko for petlje 

for student in students:
    print(student)


# ovde dobijamo samo kljuceve tj prve vrednosti 

# sa ovim dobijamo sledece vrednosti, dakle ovde kazemo da za svakog studenta uzmemo vrednosti 
# ali kazemo ostampaj mi od dictionara jednuni tj dace mi tacno onu vrenost kkoja nam treba
for student in students:
    print(student, students[student] , sep =", ")


print(students[0])
