#Q1)Write a program to check whether a number is even or odd. 

# num = int(input("enter a number"))

# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

#Q2) Write a program to check whether a number is positive, negative, or zero.

# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

#Q3) Find the largest of three numbers without using max(). 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest:", a)
# elif b >= a and b >= c:
#     print("Largest:", b)
# else:
#     print("Largest:", c)

#Q4) Find the smallest of three numbers without using min(). 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a <= b and a <= c:
#     print("Smallest:", a)
# elif b <= a and b <= c:
#     print("Smallest:", b)
# else:
#     print("Smallest:", c)

#Q5)Check whether a number is divisible by both 3 and 5.

# num = int(input("enter the number"))

# if num % 3 == 0 & num % 5 ==0:
#     print("divisible by 3 and 5")

# else :
#     print("not divisible")

#Q6)Check whether a given year is a leap year. 

# year = int(input("enter a year"))

# if year % 4 == 0:
#     print("leap year")

# else:
#     print("not a leap year")

#Q7)Check whether a given character is a vowel or consonant. 

# ch = input("enter character")

# if ch in "aeiouAEIOU":
#     print("vowel")
# else:
#     print("consonant")


#Q8)Check whether a person is eligible to vote based on age. 

# age = int(input("enter age"))

# if age>18:
#     print("can vote")
# else:
#     print("not eligible")


#Q9)Print numbers from 1 to N using a loop. 

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     print(i)

#Q10)Print all even numbers from 1 to N. 

# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i)

#Q11)Print all odd numbers from 1 to N.

# n = int(input("enter N: "))

# for i in range(1,n+1,2):
#     print(i)

#Q12)Find the sum of numbers from 1 to N. 

# n = int(input("Enter N: "))

# sum = 0

# for i in range(1, n + 1):
#     sum = sum + i

# print("Sum:", sum)

#Q13)Find the sum of even numbers from 1 to N. 

# n = int(input("enter N: "))

# sum = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum = sum + i


# print("sum : ",sum)

#Q14)Find the sum of odd numbers from 1 to N.

# n = int(input("enter N: "))

# sum = 0

# for i in range(1,n+1,2):
#         sum = sum + i


# print("sum : ",sum)

#Q15)Print the multiplication table of a given number. 


# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

#Q16) Calculate the factorial of a number using a loop. 

# n = int(input("Enter a number: "))

# fact = 1

# for i in range(1, n + 1):
#     fact = fact * i

# print("Factorial =", fact)

#Q17)Generate the Fibonacci series up to N terms. 

# n = int(input("Enter N: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a)
    
#     c = a + b
#     a = b
#     b = c

#Q18)Count the number of digits in a number.

# n = int(input("enter the number:"))

# count = 0

# while n>0:
#     n = n // 10
#     count = count + 1

# print("number of digits: ",count)


#Q19)Find the sum of digits of a number. 

# n = input("Enter number: ")

# sum = 0

# for i in n:
#     sum = sum + int(i)

# print(sum)


#Q20)Find the product of digits of a number. 

# n = input("Enter the number: ")

# product = 1

# for i in n:
#     product = product * int(i)

# print(product)



#Q21)Reverse a number without converting it into a string. 

# number = input("Enter number: ")

# reverse = ""

# for letter in number:
#     reverse = letter + reverse

# print(reverse)


#Q22) Find the largest digit in a number. 

# number = input("Enter number: ")

# largest = 0

# for i in number:
#     if int(i) > largest:
#         largest = int(i)

# print("Largest digit =", largest)

#Q23) Find the smallest digit in a number. 

# number = input("Enter number: ")

# smallest = 9

# for i in number:
#     if int(i) < smallest:
#         smallest = int(i)

# print("Smallest digit =", smallest)


#Q24)Count the even and odd digits in a number. 

# number = input("Enter number: ")

# even = 0
# odd = 0

# for i in number:
#     if int(i) % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1

# print("Even digits =", even)
# print("Odd digits =", odd)




#Q25)Check whether a number is a palindrome.

# n = input("enter a number: ")

# reverse = ""

# for letters in n:
#     reverse = letters + reverse

# print(reverse)

# if n == reverse:
#     print("palindrome")
# else:
#     print("not a palindrome")


#Q26). Check whether a number is a prime number

# n = int(input("Enter number: "))

# for i in range(2, n):
#     if n % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")


#Q27)Find all the factors of a number.

# n = int(input("Enter number: "))

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i) 



#Q28)Print all prime numbers within a given range. 


#Q29)Check whether a number is an Armstrong number


#Q30)Check whether a number is a perfect number


#Q31)Write a function to check whether a number is prime. 

# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# n = int(input("Enter number: "))

# if prime(n):
#     print("Prime")
# else:
#     print("Not Prime")


#Q32)Write a function to reverse a number.


# def reverse_number(n):
#     reverse = ""

#     for letters in n:
#         reverse = letters + reverse

#     return reverse


# n = input("Enter a number: ")

# print(reverse_number(n))


#Q33)Write a function to check a number is palindrome or not.


# def palindrome(n):
#     reverse = ""

#     for letter in n:
#         reverse = letter + reverse

#     if n==reverse:
#         return True
#     else:
#         return False

# n = input("enter number")

# if palindrome(n):
#     print("palindrome")
# else:
#     print("not palindrome")


#Q34) Write a function to generate the Fibonacci series. 


# def fibonacci(n):
#     a = 0
#     b = 1

#     for i in range(n):
#         print(a)

#         c = a + b
#         a = b
#         b = c


# n = int(input("Enter number of terms: "))

# fibonacci(n)


#Q35)


#Q36)
#Q37)
#Q38)
#Q39)
#Q40)
#Q41)
#Q42)
#Q43)
#Q44)
#Q45)
#Q46)
#Q47)
#Q48)
#Q49)
#Q50)
#Q51)
#Q52)
#Q53)
#Q54)
#Q55)
#Q56)
#Q57)
#Q58)
#Q59)
#Q60)
#Q61)
#Q62)
#Q63)
#Q64)
#Q65)
#Q66)
#Q67)
#Q68)
#Q69)
#Q70)
#Q71)
#Q72)
#Q73)
#Q74)
#Q75)
#Q76)
#Q77)
#Q78)
#Q79)
#Q80)
#Q81)
#Q82)
#Q83)
#Q84)
#Q85)
#Q86)
#Q87)
#Q88)
#Q89)
#Q90)
#Q91)
#Q92)
#Q93)
#Q94)
#Q95)
#Q96)
#Q97)
#Q98)
#Q99)
#Q100)