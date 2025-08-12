class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal): 
    def bark(self):
        print("Dog barks")

class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Duck quacks")

class Person:
    def eat(self):
        print("Person eats")

class Student(Person):  
    def study(self):
        print("Student studies")

class CollegeStudent(Student): 
    def attend_lecture(self):
        print("Attending lecture")

Dog().bark()
Dog().speak()

d = Duck()
d.fly()
d.swim()
d.quack()

cs = CollegeStudent()
cs.eat()
cs.study()
cs.attend_lecture()
