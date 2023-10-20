class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)
point.move()
point.draw()



'''-------------- Exercise ----------------------'''


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi! I am {self.name}")


person1 = Person("Breno")
person1.talk()



'''-------------------------- Inheritance --------------------------------'''

class AnimalActions:
    def walk(self):
        print("walk")

    def swim(self):
        print("swim")


class Dog(AnimalActions):
    def bark(self):
        print("bark")


class Cat(AnimalActions):
    def meow(self):
        print("Meow")


dog1 = Dog()
cat1 = Cat()

dog1.walk()
cat1.walk()

dog1.bark()
cat1.meow()