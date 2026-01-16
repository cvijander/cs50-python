# ask user for their name

name = input("Hello dock ,what is our name? ").strip().title()
print("hello, world")

# Remove whitespace from str 
#name = name.strip()  

# Remove whitespace form str and capitalize user's name
# name = name.strip().title()

# Capitalize user's name 
# name = name.capitalize()


# Split user's name into first name and last name 
first, last = name.split(" ")

# name = name.title()
#say hello to user
print (name)
print("Hello," , first)
print(f"Hello , {last}")