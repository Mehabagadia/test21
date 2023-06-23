class Bird:
    def fly(self):
         print("Bride flying")
#child class dog inherits the base class animal
class Crow(Bird):
    def cawing(self):
        print("crow cawing")
class Chick(Crow):
    def eat(self):
        print("chick eating something.....")
p= Chick()
p .eat()
p. cawing()
p. fly()