def main():
    #spacecraft = {"name":"Voyager 1", "distance": 163}
    spacecraft = {"name":"James Webb Space Telescope"}
   # spacecraft["distance"] = 0.01
   #adding new keys 
    spacecraft.update({"distance":0.01 ,"orbit" : "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    =========== REPORT ==========


    Name: TODO {spacecraft["name"]}
    Distance: TODO  {spacecraft.get("distance","Unknown")}  AU
    Orbit : {spacecraft.get("orbit", "Unknown")}


    ===============================
    """


main()