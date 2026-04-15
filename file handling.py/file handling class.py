# file_name = "note.txt"

# note = input("Enter you note:")
# file = open(file_name, "a")
# file.write(note +"\n")

# file.close()


# print("note add successfully \n")

  
# file = open(file_name, "r")
# content = file.read()
# print(content)
# file.close()




# try and except block

# try:
#     num1 = float(input("Enter you first number:"))
#     num2 = float(input("Enter you second number:"))
    
#     result = num1 / num2
#     print("the result is :", result)
    
    
# except ValueError:
#     print("Invalid input . please enter a valid number:")
# except ZeroDivisionError:
#     print("Error: division by zero is not alloweds" )
# finally:
#     print("This program is executed successfully")

#          oops  concepts questions

#create a student class with name , marks and display method
# class student :
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def display(self):
#         print("name:", self.name)
#         print("marks:",self.marks)
# s1 = student("Alice",85)
# s1.display()

# create a calculator class with add , subtract , multiply and divide method
# class calculator:
#     def add(self,a ,b):
#         return a + b
#     def subtract(self,a ,b):
#         return a - b
#     def multiple(self,a ,b):
#         return a * b
#     def divide(self,a ,b):
#         return a / b
# calc = calculator()
# print("Addition:", calc.add(10, 5))
# print("Subtraction:", calc.subtract(10, 5))
# print("Multiplication:", calc.multiple(10, 5))
# print("Division:", calc.divide(10, 5) )



# class Book:
#     def __init__(self,titile , author):
#            self.title = titile
#            self.author = author
#     def display(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
# book1.display()
           
           
        
class BankAccount:
    def __init__(self,balance = 0):
        self.balance = balance
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance = self.balance + amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount. Please enter a positive value.")
            
    def withdraw(self,amount):
        if amount > self.__balance:
             print("Insufficient funds.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid amount. Please enter a positive value.")
    def display_balance(self):
        print(f"Current balance: {self.__balance}")
        
        
        
acc = BankAccount(12000)
acc.deposit(5000)
acc.withdraw(2000)
acc.display_balance()