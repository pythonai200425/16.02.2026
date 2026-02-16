

class Person:

    def __init__(self, age):
        self.__age = age

    # Getter
    @property
    def age(self):
        return self.__age

    # Setter
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative")
        else:
            self.__age = value

p = Person(20)
print(p.age)
p.age = -20

print()

# class
# init
# str
# repr
# __magic__
# abstract
# inheritance, override
# interface
# encapsulation
# static