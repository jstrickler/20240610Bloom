#  house <- blueprint
# instance = Class()
# obj = Class()

heroes = list()   # create an instance of the list class

heroes.append("Deadpool")
heroes.append("Ironman")
heroes.insert(0, "Black Panther")

print(f"{heroes = }")

class Animal:
    def breathe(self):
        print("breathing in...breathing out")

x = Animal()
x.breathe()  #  call the .breathe() method from an instance of Animal
print()

class Mammal(Animal):
    pass

class Dog(Mammal):
    def bark(self):
        print("woof! woof!")

d1 = Dog()
d2 = Dog()
d1.bark()
d2.bark()
d1.breathe()





