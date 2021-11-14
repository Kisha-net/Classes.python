#creating a class
class MyClass:
    x = 10

#creating an object
y1=MyClass()
print(y1.x)

#the init function
class Person:
    def __init__(self, name, age):
     self.name = name
     self.age = age

p1=Person("Antoinette AKinyi" , 20)
print(p1.name)
print(p1.age)