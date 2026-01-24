def main():
    printSquare(3)



def  printSquare(size):

    # For each row in square 
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#" , end="")


        # for every row to get to new line    
        print()        


main()



# za laksi tj jednostavni nacin da se dodje do istog resenja, tako sto se u tom redu proglasi da se stampa 

def print_Square2(size):
    for i in range(size):
        print("#" * size)


# ili jos podeliti na vise grupa tj metoda i onda jedna metoda pravi redove a druge kolone 


def print_Squre3(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)



# drugfi nacin tj nacin koriscenja for petlje za dobijanje redova plus dodatak print za novi red 

def print_row1(width1):
     for _ in range(width1):
          print("#", end="")
     print()     