from time import asctime
from unicodedata import name

def menu():
    opt = '9'
    while opt != '3':

        print("1 - Employee entry. \n2 - Employee exit. \n3 - Exit menu. \n")
        print("Select an option.")
        opt = input()

        if opt == '1':
            print("Enter the name of the employee who entered")
            name = input()
            newString = str(employeeEntry(name))
            print(newString)
            saveFile(newString)

        elif opt == '2':
            print("Enter the name of the employee who exited")
            name = input()
            newString = str(employeeExit(name))
            saveFile(newString)

        elif opt == '3':
            break
        
        else:
            print("Invalid option")

def employeeEntry(name = ''):
    newString = str((f"{asctime()} - {name} - Entry"))
    return newString
    

def employeeExit(name = ''):
    print(asctime()," - ",name," - Exit")
    

def saveFile(entryOrExit = ''):
    f = open("texto.txt", "w")
    f.write(entryOrExit)

menu()
