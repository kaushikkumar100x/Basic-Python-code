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

try:
    num1 = float(input("Enter you first number:"))
    num2 = float(input("Enter you second number:"))
    
    result = num1 / num2
    print("the result is :", result)
    
    
except ValueError:
    print("Invalid input . please enter a valid number:")
except ZeroDivisionError:
    print("Error: division by zero is not alloweds" )
finally:
    print("This program is executed successfully")
    