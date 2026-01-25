# Program Name: Lab1.py (use the name the program is saved as)
# Course: IT3883/Section Module 1
# Student Name: David Williams
# Assignment Number: Assignment 1
# Due Date: 01/24/ 2026
# Purpose: Program that creates a list with springs
# Resources:

# define x for loop and creat list
x = 0
name = []

# Start loop
while x != 4:
    # show the Menu
    print("\n1 - Add name\n"
          "2 - Delete name\n"
          "3 - List all names\n"
          "4 - Exit")
    # input number for list
    x = int(input("Enter your choice: "))
    
    if x == 1:
        # adding a name to list
        add = input(f"\nEnter the name to be added: ")
        name.append(add)
        print("Name has been Added")
    elif x == 2:
        # name not in list entered
        delete = input("\nEnter the name to be deleted: ")
        if delete not in name:
            print(f"No such name exists!")
        else:
            # removing the name from list
            name.remove(delete)
            print(delete, "has been removed")
    elif x == 3:
        # print list
        print("")
        print("\n". join(name))

else:
    print("Shutting down") # exit program

