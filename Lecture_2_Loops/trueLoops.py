"""
while True:
    n = int (input("What is n? "))
    if n < 0:
         continue
    else:
         break


"""
"""
while True:
    n = int(input("What is n? "))
    if n > 0:
        break
    
      
for _ in range(n):
    print("meow")


"""

def main():
    number = getNumber()
    meow(number)


def getNumber():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break


    return n




def meow(userNumber):
    for _ in range(userNumber):
        print("meow")



main()