class Animal:
    
         def eat(self):
            print("can eat")

class Bird:

    def fly(self):
         print("can fly")
        

class Bat(Animal,Bird):
     
     def sleep(self):
          print("Bat sleep upside down")

     def bite(self):
          print("Bat Bites")
          



b = Bat()

b.fly()
b.eat()
b.sleep()
b.bite()
