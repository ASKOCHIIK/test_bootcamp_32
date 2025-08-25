def main():
    print("Hello World")
if __name__ == "__main__":
    main()

<<<<<<< HEAD
class Student:
    def __init__(self, age):
        self.__age = age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Жаш терс болбойт")
        self.__age = value
s = Student(18)
print(s.age)

s.age = 20
print(s.age)

s.age = 5

class Doniko:
    def __init__(self, name):
        self.name = name

    def Get_info(self):
        return self.name
D = Doniko('Daniel')
print(D.Get_info())

