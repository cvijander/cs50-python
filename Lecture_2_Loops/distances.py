distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10" : 80,
    "New Horizons": 58,
    "Pioneer 11" : 44
}


def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")
        #print(f"{name} is {distances.values()}")
        #print(f"{name} is {distances.items()}")
    

    for name , distance in distances.items():
        print(f"{name} is {distance}")
     


    for name in distances:
        print(f"{name} is {distances[name]}")


    for distance1 in distances.values():
        print(f"{distance1} AU is {convert(distance1)} m")     

def convert (au):
      return au * 149597870700


main()    