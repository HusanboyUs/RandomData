import random

names=['Husanboy','Aziz','Laziz','Salim','Karim','Xalim']

class RandomData():
                    
    @staticmethod
    def randomName():
        return random.choice(names)
    @staticmethod
    def randomName():
        
        return random.choice(names)

    @staticmethod
    def randomCapitals():
        capitals=['Warsaw','Tashkent','Berlin']
        return random.choice(capitals)

    def __init__(self,arg):
        self.arg=arg

#example data
class console():
    def __init__(self,arg):
        self.arg=arg
    def log(arg):
        print(arg)    