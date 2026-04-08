file_name = "note.txt"

note = input("Enter you note:")
file = open(file_name, "a")
file.write(note +"\n")

file.close()


print("note add successfully")

file = open(file_name, "r")
content = file.read()
print(content)
file.close()