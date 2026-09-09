#Q1)Create a Student class with:
# name
# age
# course
# Create one object and print all details.

# class Student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course

# student1 = Student("Asif",22,"python")

# print(student1.name)
# print(student1.age)
# print(student1.course)

#Q2)Create an Employee class with:
# name
# salary
# department
# Create an object and display the employee details


# class Employee:
#     def __init__(self,name,salary,department):
#         self.name=name
#         self.salary=salary
#         self.department=department

# employee1 = Employee("Asif",15000,"IT")

# print(employee1.name)
# print(employee1.salary)
# print(employee1.department)


#Q3)Create a Car class with:
# brand
# model
# price
# Create two objects with different values and print their details


# class Cars:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price

# car1 = Cars("jeep",2025,35)
# car2 = Cars("Lambho",23,400)

# print(car1.model)
# print(car2.brand)
# print(car1.brand)

#Q4)Student Details
# Create a Student class with:
# _init_() to store name and age
# One method display() to print the student details
# Create an object and display the details.


# class Students:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("student name:",self.name)
#         print("stdent age:",self.age)

# student1 = Students("Asif",22)

# student1.display()
       


#Q5)Create an Employee class with:
# _init_() to store name and salary
# One method show_salary() to print the employee's name and salary
# Create an object and call the method.


# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def display(self):
#         print("name:",self.name)
#         print("salary:",self.salary)

# employee1 = employee("Asif",15000)

# employee1.display()


####################################################################################################

#SLICING CONCEPT


#Q1) word = "hello"

# a= word[2:4]
# b= word[0:2] + word[4:]

# print(a)
# print(b)

#Q2) 

# word = "program"

# a= word[0:3]
# b= word[3:]

# print(a)
# print(b)


# Q3)

# word = "malayalam"
# reverse = word[::-1]

# print(reverse)


#Q4)

# word = "hello"
# reverse = ""

# for letter in word:
#     reverse = letter + reverse

# print(reverse)


#Q5)

# word = "hello"
# reverse = ""

# for letter in word:
#     reverse = letter + reverse

# print(reverse)

# if word == reverse:
#     print("It is palindrome")

# else :
#     print("It is not a palindrome")




#Q6) 3 lifts are present - lift A , lift B , lift C . a user is standing by and if they press the floors 1-5 the lift A must come and if pressed floor from 6-10 lift B must come and from 11-15 lift C comes.. write the program for it..?


# floor = int(input("enter the floor: "))

# if floor >= 1 and floor <= 5:
#     print("Lift A")
# elif floor >=6 and floor <= 10:
#     print("Lift B")
# elif floor >=11 and floor <= 15:
#     print("Lift C")
# else:
#     ("please enter a valid floor")o
