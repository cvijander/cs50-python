name = input ("What is your name? ")
"""
if name == "Harry":
    print("Griffindor")
elif name == "Hermione":
    print("Griffindor")    
elif name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")    

"""

"""
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print ("Slytherin") 
else: 
    print("Who? ")    
"""

"""
match name:
    case "Harry":
        print("Griffindor")
    case "Hermione":
        print("Griffindor")
    case "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin") 
    case _:
        print("Who?")      
"""

match name:
      case "Harry" | "Hermione" | "Ron":
           print("Gryffindor") 
      case "Draco":
            print("Slytherin")     
      case _:
            print("Who? ")      


