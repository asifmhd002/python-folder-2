#Q1)creeate a parent class animal with an eat method and child class dog with a bark method. create and object and call both methods


# class Animal:
#     def eat(self):
#         print("animal eat")


# class dog(Animal):
#     def bark(self):
#         print("dog bark")

# dog1 = dog()

# dog1.eat()
# dog1.bark()

#Q2)create a parent class vehicle with a start method and child class car with drive methods . create and object and call both methods

# class Vehicle:
#     def start(self):
#         print("vehicle started")

# class car(Vehicle):
#     def drive(self):
#         print("car started")

# obj = car()

# obj.start()
# obj.drive()

#Q3)create a parent class person with speak method and student class with study method. create obejcts and call both methods. 

# class person:
#     def speak(self):
#         print("person spoke")

# class student(person):
#     def study(self):
#         print("student is studying")

# obj = student()

# obj.speak()
# obj.study()


#Q4)Create two parent classes Father and Mother with driving() and cooking() methods. Create a Child class that inherits from both and add a playing() method. Create an object and call all three methods.

# class father:
#     def driving(self):
#         print("father is driving")

# class mother:
#     def cooking(self):
#         print("mother is cooking")

# class child(father,mother):
#     def playing(self):
#         print("child is playing")


# obj = child()

# obj.driving()
# obj.cooking()
# obj.playing()


#Q5)Create two parent classes Camera and MusicPlayer with take_photo() and play_music() methods. Create a SmartPhone class that inherits from both and add a make_call() method. Create an object and call all three methods.


# class camera:
#     def takephoto(self):
#         print("camera took photo")

# class musicplayer:
#     def playmusic(self):
#         print("musicplayer is playing music")

# class smartphone(camera,musicplayer):
#     def makecall(self):
#         print("phone is making a call")

# obj = smartphone()

# obj.takephoto()
# obj.playmusic()
# obj.makecall()

#Q6)Create a parent class Animal with an eat() method. Create a child class Mammal with a walk() method. Create another child class Dog with a bark() method. Create a Dog object and call all three methods.


# class animal:
#     def eat(self):
#         print("animal eats")

# class mammal:
#     def walk(self):
#         print("mammals is walking")

# class dog(animal,mammal):
#     def bark(self):
#         print("dog is barking")

# dogobj = dog()

# dogobj.eat()
# dogobj.walk()
# dogobj.bark()


#Q7)Create a parent class School with a study() method. Create a child class Student with a attend_class() method. Create another child class CollegeStudent with a project() method. Create a CollegeStudent object and call all three methods.


# class school:
#     def study(self):
#         print("school study")

# class student(school):
#     def attendclass(self):
#         print("student attends class")

# class collegestudents(student):
#     def project(self):
#         print("collegestudents has done the project")

# obj = collegestudents()

# obj.study()
# obj.attendclass()
# obj.project()

#Q8)Create a parent class Animal with an eat() method. Create two child classes Dog and Cat. Add bark() to Dog and meow() to Cat. Create objects of both classes and call their own methods and the inherited eat() method.

# class animal:
#     def eat(self):
#         print("animal is eating")

# class dog(animal):
#     def bark(self):
#         print("dog barking")

# class cat(animal):
#     def meow(self):
#         print("cat meowing")

# dogobj = dog()
# catobj = cat()

# dogobj.eat()
# dogobj.bark()

# catobj.eat()
# catobj.meow()


#Q9)Create a parent class Vehicle with a start() method. Create two child classes Car and Bike. Add drive() to Car and ride() to Bike. Create objects of both classes and call all applicable methods

# class vehicle:
#     def start(self):
#         print("vehicke started")

# class car(vehicle):
#     def drive(self):
#         print("car driving")

# class bike(vehicle):
#     def ride(self):
#         print("bike ride")

# carobj = car()
# bikeobj = bike()

# carobj.start()
# carobj.drive()

# bikeobj.start()
# bikeobj.ride()


#Q10)Create a Python program for a Bank Account system.
# Use Encapsulation to keep the account balance private.
# Use Inheritance to create SavingsAccount from BankAccount.
# Use Polymorphism to define a calculate_interest() method differently for different account 

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def calculate_interest(self):
#         return 0


# class SavingsAccount(BankAccount):
#     def calculate_interest(self):
#         return self.get_balance() * 0.05


# class CurrentAccount(BankAccount):
#     def calculate_interest(self):
#         return self.get_balance() * 0.02


# savings = SavingsAccount(10000)
# current = CurrentAccount(10000)

# print("Savings Account Balance:", savings.get_balance())
# print("Savings Interest:", savings.calculate_interest())

# print("Current Account Balance:", current.get_balance())
# print("Current Interest:", current.calculate_interest())


# # Q11)Create a Python program for a Vehicle system.
# Use Encapsulation to keep the vehicle's speed private.
# Use Inheritance to create Car and Bike from Vehicle.
# Use Polymorphism so start() behaves differently for Car and Bike.



# class Vehicle:
#     def __init__(self,speed):
#         self.__speed = speed

#     def get_speed(self):
#         return self.__speed

#     def start(self):
#         print("vehicle started")

# class Car(Vehicle):
#     def start(self):
#         print("car started")

# class Bike(Vehicle):
#     def start(self):
#         print("bike started")

# car = Car(120) 
# bike = Bike(80)

# print("Car Speed:", car.get_speed())
# car.start()

# print("Bike Speed:", bike.get_speed())
# bike.start()



########################################################################################


#Employee Management System Create an Employee Management System using Python OOP. Create the following classes: 
# • Employee 
# • Developer 
# • Manager 
# The program should provide the following features: 
# 1. Add employee 
# 2. Display employee details 
# 3. Calculate salary 
# 4. Display employee role 
# 5. Implement different salary calculations for Developer and Manager



class Employee:
    def __init__(self,name,empid,salary):
        self.__name = name
        self.__empid = empid
        self.__salary = salary

    def get_details(self):
        print("Name:",self.__name)
        print("Emp_id:",self.__empid)

    def calculate_salary(self):
        return self.__salary

    def employee_role(self):
        print("Role: Employee")

class Developer(Employee):
    def calculate_salary(self):
        return self._Employee__salary * 0.5 + self._Employee__salary

    def employee_role(self):
        print("Role:Developer")

class Manager(Employee):
    def calculate_salary(self):
        return self._Employee__salary + 10000

    def employee_role(self):
        print("Role:Manager")

employee = Employee("Asif",100,10000)
developer = Developer ("Vijay",101,10000)
manager = Manager("Ram",102,10000)

employee.get_details()
print("salary:",employee.calculate_salary())
employee.employee_role()

print()

developer.get_details()
print("salary:",developer.calculate_salary())
developer.employee_role()

print()

manager.get_details()
print("salary:",manager.calculate_salary())
manager.employee_role()

