class Animal:
    def __init__(self, name):
        self.name = name

    def enterGarden(self):
        print("The animal has entered your garden")
        return   

    def bite(self):
        print("The animal bites you")
        return

    def eat(self):
        print("The animal eats your garden")
        return

    def run(self):
        print("The animal runs away")
        return

    def dies(self):
        print("You've killed the animal")
        return



class Fox(Animal):
    pass

class Raccoon(Animal):
    pass

class Snake(Animal):
    pass

class Squirrel(Animal):
    pass

class Rabbit(Animal):
    pass

