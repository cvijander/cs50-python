def main():
    difficulty = input ("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter  a valid difficulty")
        return


    players = input("Multiplayer or Single-player? ")
    if not ( players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players")
        return 


    #if difficulty == "Difficult":
     #   if players == "Multiplayer":
      #      recommend("Poker")
       # elif players == "Simgle-player":
        #    recommend("Klondike")          

    if difficulty == "Difficult" and players == "Multiplayer":
         recommend("Poker") 

    elif difficulty == "Difficult" and players =="Single-player":
        recommend("Klondike")

    #elif difficulty == "Casual":
     #   if players == "Multiplayer":
      #      recommend("Hearsts")
       # elif players == "Single-player":
        #    recommend("Clock")  

    elif difficulty =="Casual" and players == "Multiplayer":
        recommend("Hearsts")    
    else:
         recommend("Clock")    
                  


    

def recommend(game):
    print ("You should play " , game)            






main()