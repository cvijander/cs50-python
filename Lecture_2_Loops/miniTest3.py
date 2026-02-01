def main():
   user_input()


user_list = []

def user_input():
     round = 5 
     for i in range(5):
         number = input("Enter a number ")
         int_number = int(number)
         user_list.append(int_number)  

    
     bigger_than_5(user_list)  
          

def bigger_than_5(user_list):
    for numb in user_list:
        if numb > 5 :
            print(f"{numb}")


main()    