WORDS = {"PAIR":4, "HAIR": 4, "CHAIR":5 , "GRAPHIC": 7}
#UserWORDS = {"A", "I", "P", "C", "R", "H", "G"}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0 :
         print(f"{len(WORDS)} words left! ")
         guess = input("Guess a word: ")
         filteredGuess = guess.strip().upper()

        # if UserWORDS.keys() in filteredGuess(): 
         #    filteredGuess = UserWORDS.pop(UserWORDS.keys())

        # TODO:  check is guess in dictionary 
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



main()