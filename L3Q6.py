#need to solve
class Animal:
    def sound(self):
        return "Animal makes sound"

class carnivore:
    def eat(self):
        return "eats meat"

class tiger(Animal,carnivore):
    def run(self):
        return "runs fast"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

class Puppy(Dog):
    def bark_jr(self):
        return "Puppy barks meekly"

# Example usage
puppy = Puppy()# multilevel inheritane
print(puppy.sound())
print(puppy.bark())
print(puppy.bark_jr())

dog= Dog() #inheritance
print(dog.sound())

tiger_1=tiger()
print(tiger_1.run())
print(tiger_1.eat())