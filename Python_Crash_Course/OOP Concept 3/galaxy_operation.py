
class ourgalaxy():

    def __init__(self,planet):
        self.planet=planet
    
    def information(self):
        # print("You choose :" + self.planet)
        if(self.planet == 'mecury'):
            print("Mercury is the smallest and innermost planet in the Solar System. Its orbital period around the Sun of 87.97 days is the shortest of all the planets in the Solar System."
                  " It is named after the Roman deity Mercury, the messenger of the gods.")
        elif(self.planet == 'venus'):
            print("Venus is the second planet from the Sun, orbiting it every 224.7 Earth days.[13] It has the longest rotation period (243 days) of any planet in the Solar System and rotates in the opposite direction to most other planets (meaning the Sun rises in the west and sets in the east)."
                  "[14] It does not have any natural satellites. It is named after the Roman goddess of love and beauty.")
        elif(self.planet == 'earth'):
            print("Earth is the third planet from the Sun, and the only astronomical object known to harbor life. According to radiometric dating and other sources of evidence, Earth formed over 4.5 billion years ago."
                  " Earth's gravity interacts with other objects in space, especially the Sun and the Moon, Earth's only natural satellite")
        elif(self.planet == 'mars'):
            print("Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System after Mercury.")
        elif(self.planet == 'jupiter'):
            print("Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a giant planet with a mass "
                  "one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined.")
        elif(self.planet == 'saturn'):
            print("Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius about nine times that of Earth."
                  " It has only one-eighth the average density of Earth, but with its larger volume Saturn is over 95 times more massive.")
        elif(self.planet == 'uranus'):
            print("Uranus is the seventh planet from the Sun. It has the third-largest planetary radius and fourth-largest planetary mass in the Solar System. Uranus is similar in composition to Neptune, and both have "
                  "bulk chemical compositions which differ from that of the larger gas giants Jupiter and Saturn.")
        elif(self.planet == 'neptune'):
            print("Neptune is the eighth and farthest known planet from the Sun in the Solar System. In the Solar System, it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet."
                  " Neptune is 17 times the mass of Earth, slightly more massive than its near-twin Uranus. ")
        else:
            print("There is no planet in the galaxy that  you entered")

class planetofgalaxy(ourgalaxy):

    def __init__(self,planet):
        self.planet=planet
        super().__init__(self.planet)


    def planetname(self):
        print("You choose : " + self.planet)