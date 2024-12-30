class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
x = Person('Mike', 25)
y = Person('Sarah', 27)
z = Person('Mike', 25)

print(x==z)