#Q1)In a banking application, how would you prevent users from directly modifying their account balance? 

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount    

#     def withdraw(self, amount):
#        if (0 < amount) and (amount <= self.__balance):
#             self.__balance -= amount

#     def get_balance(self):
#         return self.__balance


# account = BankAccount(10000)

# account.deposit(5000)
# account.withdraw(14000)

# print("Balance:", account.get_balance())


#Q2)In a login system, how would you protect a user's password from direct access?

# class user:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password

#     def checkpassword(self, password):
#         return self.__password == password

# userdet = user("Asif", "12345678")

# print(userdet.checkpassword("12345678"))


#Q3)In an employee management system, how would you prevent direct modification of an employee's salary?

# class Employee:

#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self, salary):
#         if salary > 0:
#             self.__salary = salary


# employee = Employee("Asif", 50000)

# print(employee.get_salary())

# employee.set_salary(60000)

# print(employee.get_salary())


#Q4)In a student management system, how would you ensure that marks can only be between 0 and 100? 

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks

#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Marks must be between 0 and 100")


# student = Student("Asif", 85)

# print(student.get_marks())

# student.set_marks(95)

# print(student.get_marks())

#Q5)In an ATM application, how would you protect the customer's PIN

# class Atm:
#     def __init__(self,pin):
#         self.__pin = pin

#     def checkpin(self,pin):
#         return self.__pin == pin

# atm = Atm(1234)
# print(atm.checkpin(1234))

#Q6)In an e-commerce application, how would you prevent a product's price from being set to a negative value? 

# class product:
#     def __init__(self,price):
#         self.__price = price

#     def getprice(self):
#         return self.__price

#     def setprice(self,price):
#         if price >=0:
#             self.__price = price

#         else:
#             print("price cannot be negative")


# Product = product(500)

# print(Product.getprice())

# Product.setprice(200)

# print(Product.getprice())






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



# class Employee:
#     def __init__(self,name,empid,salary):
#         self.__name = name
#         self.__empid = empid
#         self.__salary = salary

#     def get_details(self):
#         print("Name:",self.__name)
#         print("Emp_id:",self.__empid)

#     def calculate_salary(self):
#         return self.__salary

#     def employee_role(self):
#         print("Role: Employee")

# class Developer(Employee):
#     def calculate_salary(self):
#         return self._Employee__salary * 0.5 + self._Employee__salary

#     def employee_role(self):
#         print("Role:Developer")

# class Manager(Employee):
#     def calculate_salary(self):
#         return self._Employee__salary + 10000

#     def employee_role(self):
#         print("Role:Manager")

# employee = Employee("Asif",100,10000)
# developer = Developer ("Vijay",101,10000)
# manager = Manager("Ram",102,10000)

# employee.get_details()
# print("salary:",employee.calculate_salary())
# employee.employee_role()

# print()

# developer.get_details()
# print("salary:",developer.calculate_salary())
# developer.employee_role()

# print()

# manager.get_details()
# print("salary:",manager.calculate_salary())
# manager.employee_role()

