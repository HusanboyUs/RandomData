import random


names=['Husanboy','Alexander','Aziz','Laziz','Salim','Karim','Xalim','Adam','Ann','Alex','Aston','Ali','Akash','Andres','Agata','Bob','Ben','Bete','Calvin',
'Chack','Chick','Caterina','Cabella','Dmitry','Dony','Doston','Dennis','Elon','David','Fredirich','Fedya','Fitrat','Ghandi','Jeck','Jason','Klain','Kevin',]

#amount of gmails increase as list of names increases
gmail_l='@gmail.com'
languages=['polish','uzbek','latin','russian','greek','arabic','hindi','korean','japananese','chinese','norwish','dutch','spain','portugal','Mongol','Kazakh'
, 'Turkish','Ukraine','Kygrzy','Tajik','Turkman','Pakistanian','Azarbeijan']
brands=['Kfc',"McDonald's",'Glovo','Uber','Apple','Micrasoft','Gucci']
cars=['BMW','Audi','GM','Ferrari','Lamborghini','Lexsus','Nissan','Mercedez','Ravon','Chevrolet','Fiat','Porch','Tesla','Scoda']
subjects=['math','sketch','Literature','Art','Global Languages']
websites=['google','python.org','kun.uz','tesla','facebook','instagram','linkedIn','Hola','Hulu','Amazon','Netflix','Youtube']
#password generator function
lower="abcdefghijklmnopqrstuvxyzw"
numbers="0123456789"
upper="ABCDEFGHIJKLMNOPQRSTUVXYZW"
all=lower+upper+numbers
length=8
password="".join(random.sample(all,length))


class randomdatagen():          
    @staticmethod
    def randomName(arg,tk='g'):
        print(arg)
        if arg==1:
            return random.choice(names)
        else:
            return 'not working'    
            
        #argument="".join(random.sample(names,arg))
        #return random.choice(names)
            
    @staticmethod
    def randomGmail():
        get_name=random.choice(names)
        return get_name+gmail_l

    @staticmethod    
    def randomLanguage():
        return random.choice(languages)

    @staticmethod 
    def randomBrand():
        return random.choice(brands)

    @staticmethod 
    def randomCar():
        return random.choice(cars)
    
    @staticmethod 
    def randomWebsite():
        return random.choice(websites)  
    
    @staticmethod 
    def randomPassword():
        return password    
    
    @staticmethod
    def numbers(arg):
        for i in range(0,arg):
            return password 
          

#example data
class console():
    def __init__(self,arg):
        self.arg=arg
    def log(arg):
        print(arg)    