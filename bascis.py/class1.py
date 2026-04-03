#add two number

# a = 4
# b = 5
# sum = a+b
# print(sum)

# user define 

# num1 = float(input("Enter a number here :"))
# num2 = float(input("Enter a another  number here :"))
# sum = num1 + num2
# print("Result of numbers :",  sum)
    
    
# print("hello")



# find the squar root

# num = float(input("Enter the any number :-"))
# squ = num**2
# print("The result of you number :- " , squ)

# find the squar root with the help of math module


# import math
# num = int(input("Enter the number :-"))
# sr = math.sqrt(num)
# print(sr)


#calculate the area of triangle 


# base = float(input("Enter the base number :-"))
# length = float(input("Enter the length number :-"))
# triangle = 0.5 * base * length
# print("The result of triangle :- ", triangle)


# swap two numbers 

# a = float(input("Enter the number first :-"))
# b = float(input("Enter the number second :-"))

# a , b = b , a
# print("result :-", a )
# print("result :-", b )


#31/03/2026===================================================================================================


# kilometer to meter

# a = float(input("Enter the meter measurement amount :-"))
# km = a/1000
# print(f"meter is convert into a kilometers  result  = {km}km" )



#number cheak is negative and is postive

# a = float(input("Enter the number and find this type of number :-"))
# if(a>0):
#     print(f"{a} This number is postive ")
# elif(a == 0):
#     print(f"{a} This is a nutral number")
# else:
#     print(f"{a} This number is negative")


#cheak this number is odd


# a = input("Enter the multiple numbers :-")
# b = list(map(int,a.split()))
# for oe in b:
#     if oe % 2 ==0:
#         print(f"its a Even number. {oe}")
#     else:
#         print(f"its a odd number. {oe}")
# print("this finish")

# check the leap year or not

# a = input("Enter the years :-")
# b = list(map(int,a.split()))
# for year in b:
#     if(year%4==0 and year%100!=0 )or (year%400==0):
#         print(f"{year}its leap year")
    
#     else:
#         print(f"{year} its not a leap year")
    
    
    # find the largest amonge three numbers
    
    
# a = int(input("Enter a number first :"))
# b = int(input("Enter a number second :"))
# c = int(input("Enter a number third :"))
# if a>b and a>c :
#     print(f"{a} its a gratest number")

# elif b>a and b>c :
#     print(f"{b} its a gratest number")
    
# else:
#     print(f"{c} its a gratest number")



# prime numbers

# a = int(input("Enter the number :"))
# if a<=1:
#     print("not a prime number")
# else:
#   for i in range(2,a):
#     if (a%i == 0 ):
#         print(f"{a} its not prime number")
#         break
#     else:
#         print("Prime number")
# print("final result :")




# genrate randome number

# import random

# num = random.randint(0,10)
# print(num)

# WAP to all prime number in an interval


# lower = int(input("Enter the lower number"))
# upper = int(input("Enter the upper number"))

# for num in range(lower , upper+1):
#     if num>1:
#            for i in range(2 , num):
#                if(num%i == 0):
#                 break
#            else:
#             print(num)

#onvert to celsius to fahrenheit

# cel = int(input("Enter the fehrenheit:-"))
# result = ((cel-32) *(3/9))
# print(f" Celsius Result is :- {result}")

# factorial by loop


# a = int(input("Enter the factorial number:-"))
# fact = 1
# if a<0:
#     print("factorial of 0 dose not exist ")
# if a == 0:
#     print("factorial of 0 is ",1)
# if a>0:
#     for i in range(1,a+1):
#      fact = fact*i
# print("factorial of given number is :-", fact)


# by fraction

# num =  int(input("Enter the factorial number"))
# def factorial(a):
#     if a == 0:
#         return 1
#     else:
#         return ((a)*factorial(a-1))  
    
# result = factorial(num)
# print("the factorial of the given number ", result)


# multiplication of the number

# a = int(input("Enter the number:-"))
# for i in range(1,10+1):
#     print(a*i)


# fibonacci sequence 

# num = int(input("Enter the number :-"))

# a = 0
# b = 1
# c = a+b
# for i in range(1,num+1):
#      c = a + b
#      b = a
#      a = c
#      print(c)



# Armstrong number


num = int(input("Enter the numbers :-"))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    sum+= digit**3
    
    temp//=10
    if num == sum:
        print("its a Aarmstrong number", num)
        break
else:
     print("its not Armstrong number", num)  # its not complete this code
