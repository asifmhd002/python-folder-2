#Q1)
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()


#Q2)
#     *
#    **
#   ***
#  ****



# for i in range(1,5):
#     for j in range(4-i):
#         print(" ",end="")

#     for j in range(i):
#         print("*",end="")

#     print()



#Q3)

#    *
#   ***
#  *****
# *******


# for i in range(1,5):
#     for j in range(4-i):
#         print(" ",end="")

#     for j in range(2*i-1):
#         print("*",end="")

#     print()



#Q4)

# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *

# for r in range(7):
#     for c in range(8):
          

#           if((c==0 or c==7) or  
#             ((c==1 or c==6) and (1 <=r<= 5)) or 
#             ((c==2 or c==5)and (2 <=r<= 4)) or 
#             ((c==3 or c==4) and r==3)):
#             print("*",end="")

#           else:
#             print(" ",end="")

#     print()


#Q5)

#   *  
#  * * 
# *****
# *   *
# *   *
# *****

# for r in range(6):
#     for c in range(5):


#         if((r==2 or r==5) or
#            ((c==0 or c==4) and (2 <=r<= 5)) or
#            (r==1 and (c==1 or c==3)) or
#             (r==0 and c==2)):
#             print("*",end="")
#         else:
#             print(" ",end="")

#     print()
 

#Q6)

#  *** 
#  *** 
#  *** 
# *****
# *****
# *****


# for r in range(6):
#     for c in range(5):

#         if((3 <=r<= 5) or
#            (r<=2 and (1 <=c<= 3))):
#             print("*",end="")

#         else:
#             print(" ",end="")


#     print()


#Q7)

# *******
#  ***** 
#   ***  
#    *   
#   ***  
#  ***** 
# *******



for r in range(7):
    for c in range(7):


        if((r==0 or r==6) or ((r==1 or r==5) and 1<=c<=5) or ((r==2 or r==4) and 2<=c<=4) or (r==3 and c==3)):
            print("*",end="")
        else:
            print(" ",end="")

    print()