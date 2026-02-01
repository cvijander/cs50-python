def main():
    number()


def number():
    user_number = input("Please enter a number ")    
    numb = int (user_number)
    even_or_odd(numb)


def even_or_odd(n):
    if (n % 2 == 0): 
      print(f"This is  {n} is even number ")

    else:
       print(f"This {n} is odd ")



main()    