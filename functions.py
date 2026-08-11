# def add(a,b):
#     return(a+b)
# a=add(3,5)
# print(a)



# def add(a,b):
#     return(a+b)

# result=add(6,7)
# print(result)   
 

# def add(*arg):
#     return arg

# a=add(1,2,3,4,5,6,7,8,9)
# print(a)


# def show(**kwargs):
#     print(kwargs)

# show(name="Asif", age=22, course="FSP+DA")


# def numbers(**kwargs):
#     print(len(kwargs))

# numbers(name="asif",age=22,course="cse")






##############################  PRACTICE QUESTIONS #############################





# Q1)A shop wants to calculate the final price of a product after applying a discount. Create a function to perform this task.

# def finalprice(price,discount):
#     discountamount = price * discount/100
#     finalprice = price - discountamount
#     return finalprice

# result = finalprice(1000,10)
# print(result)


# Q2)A school wants to check whether a student has passed based on their marks. Create a function for this requirement.


# def result(marks):
#     if marks > 60:
#         return "passed"
#     else:
#         return "failed"

# result = result(70)
# print(result)


#Q3)A bank wants to calculate the amount a customer will receive after adding interest to their savings. Create a function for this task.



# def final(amount, intr):
#     finalamount = amount + (amount * intr / 100)
#     return finalamount

# result = final(10000, 5)
# print(result)


#Q4)A company wants to calculate an employee's monthly salary after adding allowances and deducting expenses. Create a function.


# def final(salary,expenses,allowances):
#     finalsalary = salary + allowances - expenses
#     return finalsalary

# result = final(50000,5000,10000)
# print(result)


#Q5)A supermarket wants to calculate the total bill for several products. Create a function that can handle any number of product prices.

# def final(*price):
#     total = sum(price)
#     return total

# result  =final(100,30,78,12,34)
# print(result)


#Q6)A school needs to find the highest mark among several students. Create a function that can accept multiple marks.

# def final(*marks):
#     return max(marks)

# result = final(100,30,40,23,89)
# print(result)


#Q7)A website needs to check whether a username is valid. Create a function that performs the required validation.

# def final(username):
#     if len(username) > 8:
#         return "username is valid"
#     else:
#         return "username not valid"

# result = final("sdhnuib")
# print(result)
 

#Q8)A mobile application needs to calculate the total cost of several purchased items. Design a suitable function.


# def final(*cost):
#     return sum(cost)

# result = final(100,234,4567,897)
# print(result)


#Q9)A school wants to display complete student information such as name, age, course, and mark. Create a suitable function using keyword arguments

# def final(**kwargs):
#     print(kwargs)

# final(Name="asif",age=23,course="FP+DA",marks=450)


#Q9)A company wants to generate an employee profile where different details may be provided for different employees. Create a function that can accept a variable number of details.

# def final(**kwargs):
#     print(kwargs)

# final(Name="asif",age=23,course="FP+DA",marks=450)
# final(Name="asif",age=23,course="FP+DA",marks=450)

#Q10)A food delivery application wants to calculate the final bill after adding delivery charges and applying a discount. Create a function.

# def final(amount,dcharge,discount):
#     finalbill = amount + dcharge - discount
#     return finalbill

# result = final(500,50,100)
# print(result)


#Q11)A college wants to determine a student's grade from their mark. Create a function that performs this task.

# def final(mark):

#     if mark>90:
#         return "Grade A"
#     if mark>80:
#         return "GRADE B"
#     if mark>70:
#         return "GRADE C"
#     if mark>60:
#         return "GRADE D"
#     else:
#         return "FAILED"

# result= final(45)
# print(result)


#Q12)A password system wants to check whether a password contains at least 8 characters. Create a function for this requirement.

# def final(password):
#     if len(password)>=8:
#         return "password vaild"
#     else:
#         return "password invalid"
# result = final("skjfsdbhj")
# print(result)

#Q13)A number game asks the user to enter a number and wants to determine whether it is even or odd. Create a function to perform the checking

# def final(number):
#     if number % 2==0:
#         return "even"
#     else:
#         return "odd"

# number = int(input("enter the number:"))
# result = final(number)
# print(result)

#Q14)A shopping application wants to find the most expensive item from a list of products. Create a function for this task.

# def final(*item):
#     return max(item)


# result = final(123,3456,890,456.3200)
# print(result)


#Q15)A company wants to calculate the average performance score of an employee from several scores. Create a function that accepts multiple values.

# def final(*scores):
#     return sum(scores)/len(scores)

# scores=[]

# for i in range(5):
#  score = int(input("enter the scores"))
#  scores.append(score)

# result = final(*scores)
# print("Average score:",result)



#Q16)A text-processing application needs to count how many vowels are present in a user's sentence. Create a function for this requirement.

# def final(sentence):
#     count = 0

#     for letter in sentence:
#         if letter.lower() in "aeiou":
#             count += 1

#     return count


# sentence = input("Enter the sentence: ")

# result = final(sentence)
# print("No of vowels:", result)



#Q17)A school attendance system wants to calculate the attendance percentage of a student and determine whether the student is eligible for the examination. Create a function.

# def final(attendance):
#     if attendance>75:
#         return"eligible to write exam"
#     else:
#         return"not eligible to write the exam"

# attendance = int(input("enter the attendance"))

# result = final(attendance)
# print(result)


#Q18)A banking application wants to check whether a customer can withdraw a requested amount based on their account balance. Create a function.

# def final(amount,withdrawamount):
#     if withdrawamount <= amount:
#         return "transaction successful"
#     else:
#         return "transaction Failed"

# withdrawamount = int(input("enter the amount to withdraw:"))

# result  =final(50000,withdrawamount)
# print(result)


#Q19)A small billing application needs to accept customer details such as name, phone, address, and email, even though some customers may provide additional information. Create a suitable function using keyword arguments.


# def details(**kwargs):
#     return kwargs

# name= input("enter name:")
# phone= int(input("enter phone number:"))
# adress= input("enter the address:")
# email= input("enter email:")

# result=details(
#     name=name,
#     phone=phone,
#     adress=adress,
#     email=email
# )
# print(result)
