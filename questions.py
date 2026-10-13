#Q1) fiboniace series
     
# def fibonacci(n):
#     a = 0
#     b = 1

#     for i in range(n):
#         print(a)

#         c = a + b
#         a = b
#         b = c


# n = int(input("enter number"))

# fibonacci(n)


#Q2) split the word hello (ll , heo)

# word = "hello" 
# a = word[2:4]
# b = word[0:2] + word[4]

# print(a)
# print(b)


#Q3)find avg element of list

# numbers = [1,2,3,4,5,6,7]
# total = sum(numbers)
# average = total / len(numbers)

# print(average)


#Q4)student management system


# class students:
#     def __init__(self,name,age,course,email,year):
#         self.name=name
#         self.age=age
#         self.course=course
#         self.email=email
#         self.year=year

#     def display(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
#         print("Course: ",self.course)
#         print("E-mail: ",self.email)
#         print("Year: ",self.year)


# student1 = students("Asif",22,"CSE","asif@gmail.com",2022)

# student1.display()

# percent = int(input("Enter your percent(%): "))

# if percent > 50:
#     print("Congrats",student1.name)
# else:
#     print("Better luck next time",student1.name,", Sorry for it and try harder next time.")
        

#Q5)PalPrime


# n = input("Enter number: ")

# # Palindrome
# reverse = ""

# for letter in n:
#     reverse = letter + reverse

# # Prime
# n = int(n)
# prime = True

# for i in range(2, n):
#     if n % i == 0:
#         prime = False
#         break
# else:
#     prime = True

# # Palindrome + Prime
# if n == int(reverse) and prime:
#     print("Palindromic Prime")
# else:
#     print("Not Palindromic Prime")


#Q6)
# ATM PIN Attempts.Allow a user to enter a PIN, Maximum 3 attempts
# Correct PIN → "Access Granted", Three wrong attempts → "Card Blocked".Use a while loop.


# correctpin = "1234"
# attempt = 0

# while attempt < 3:
#     pin =input("Enter PIN: ")

#     if pin == correctpin:
#         print("Access Granted")
#         break
#     attempt = attempt + 1
#     print("Wrong PIN")

# else:
#     print("Card Blocked ")


#Q7)Guess the Number

# Create a number guessing program.

# Requirements:

# Secret number = 50
# User gets 5 attempts
# Tell "Too High" or "Too Low"
# Stop immediately when the answer is correct
    

# correctnumber = 50
# attempts = 0

# while attempts < 5:
#     number = int(input("Enter number: "))

#     if number == correctnumber:
#         print("Correct")
#         break

#     elif number > correctnumber:
#         print("Too High")

#     else:
#         print("Too Low")

#     attempts = attempts + 1

# else:
#     print("Out of attempts")


#Q)Print nos from 1 to 5 using recursion


# def numbers(n):
#     if n > 5:
#         return

#     print(n)
#     numbers(n + 1)

# numbers(1)

#Q)Create a list of numbers and print thier squares

# l=[1,2,3,4,5]
# for x in l:
#     print(x**2)

#Q)Create a list of numbers and find the even nos and odd nos from it using list comprehension.

# l=[1,2,3,4,5,6,7,8,9,10]
# print([x for x in l if x%2 ==0])
# print([x for x in l if x%2 !=0])

#Q) using yield and generators print nos

# def numbers():
#     yield 1
#     yield 2
#     yield 3

# a = numbers()

# print(next(a))
# print(next(a))









