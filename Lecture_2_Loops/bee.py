WORDS = {"PAIR":4, "HAIR": 4, "CHAIR":5 , "GRAPHIC": 7}
#UserWORDS = {"A", "I", "P", "C", "R", "H", "G"}
#UserWORDS = ["A", "I","P", "C","R","H","G"]



def main():
    # kopija  sluzi za ispis kasnije koje smo reci imali u recniku 
    ALL_WORDS_BACKUP = WORDS.copy() 
    
    # pocetni deo ekrana 
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    # petlja da se uzmu slova od korisnika 
    while len(WORDS) > 0 :
         print(f"{len(WORDS)} words left! ")
         guess = input("Guess a word: ")
         filteredGuess = guess.strip().upper()

         # kopija slova samog recnika koje imamo u ponudi 
        # ALL_UserWORDS_BACKUP = UserWORDS.copy()

         # provera da li je rec koje je korinsk uneo ima to slovo iz recnika 
         #valid_word = True
         #for letter in filteredGuess:
          #  if  letter in ALL_UserWORDS_BACKUP:
           #     ALL_UserWORDS_BACKUP.remove(letter)
           # else:
            #   print(f"Error, there is not such a {letter} ili letter does not exists.")   
             #  valid_word = False
             #  break

        # TODO:  check is guess in dictionary 
         #if valid_word:
         if filteredGuess == "GRAPHIC":
              WORDS.clear()
              print("You have won!")
          
           
         if filteredGuess in WORDS.keys():
               points = WORDS.pop(filteredGuess)
            # sporiji ali mozda logicniji nacin za C# jeste da prvo poene prebacimo 
            # points = WORDS[filteredGuess]
            # drugi deo kad smo nasli poene da obrisemo taj kljuc 
            # del WORDS[filteredGuess]

            # dakle to sve menja funkcija points = WORDS.pop(filteredGuess)

               print(f"Good job. You scored {points} points.")


    print("That's the game!")  

    for word, points in ALL_WORDS_BACKUP.items():
        print(f"{word} was worth {points} points.")   



main()