class person:
    def __init__(self, name, age):
     self.name = name
     self.age = age

p1 =person("shahzaib",23)
print(p1.name)
print(p1.age)

class Animal:
    def __init__(self, name,legs):
        self.name=name
        self.legs=legs
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name,2)
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name, 4)

sparrow = Bird("sparrow")
dog = Mammal("dog")
print(f"{sparrow.name} has {sparrow.legs} legs.")
print(f"{dog.name} has {dog.legs} legs.")