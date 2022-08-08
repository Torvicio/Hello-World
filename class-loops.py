# Practice on loops
# Control K + C = Comment out line
# Control / = takes out comment
# to see directorys only : ls -d */

# i = 3
# while i !=0:
#     print (i)  
#     print("Meow")
#     # i = i-1
#     # or use this convention below
#     i -=1

# for i in [0, 1, 2]:
#     print (i)
#     print ("Meow")
# just for fun - the numnbers in i are irrelevant
#  - it still iterates through the loop
# for i in ["Milk", "Cow", 2]:
#     print (i)
#     print ("Meow")

# for i in range (3):
#     print("Meow")
# pythonic improvement - if varialble not needed use _
# for _ in range (3):
#     print("Meow")

# the \n escape sequence cleans up the output, the end =""
# cleans up the last line
# print ("meow\n" *3, end="")

# One solution to asking for input
# while True:
#     n = int(input("What's n?: "))
#     if n <0:
#         continue
#     else: 
#         break
# better solution 
# while True:
#     n = int(input("What's n?: "))
#     if n >0:
#         break
# for _ in range (n):
#     print ("Meow")
# meow function sends 3 to n - damn this is confusing
# def main ():
#     number = get_number() 
#     meow(number)
# this will not return the number until it's positive - 
# If text, it breaks, otherwise 
# if integer less 0 or less, it will continue to ask the question
# def get_number():
#     while True:
#         n = int(input("What's n?: "))
#         if n >0:
#             return n

# def meow(n):
#     for _ in range (n):
#         print ("Meow")

# main ()

# lists 
students = ["Herminone","Harry","Ron"]
# print (students) # works
# print (students [0])
# for student in students: 
#     print (student)
# a different way of doing it:
#students = ["Herminone","Harry","Ron"]
# for i in range (len (students)):
    # print (i, students [i])
    # print (i+1, students [i])
# Dictionanry - key and value  {}
students = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindir",
    "Draco": "Slytherin"
}
# print(students ["Hermione"])
# print(students ["Harry"])
# print(students ["Ron"])
# print(students ["Draco"])

# for student in students:
#     # print(students [student])
#     print (student,":", students[student])
#     # or 
#     print (student, students [student],sep=":")

# new stuff lists and dictionary
# students = [
#     {"name": "Hermione","house": "Gryffindor","patronus": "Otter"},
#     {"name": "Harry","house": "Gryffindor","patronus": "Stag"},
#     {"name": "Ron","house": "Gryffindor","patronus": "Jace Russel terrier"},
#     {"name": "Hermione","house": "Gryffindor","patronus": None}
# ]
# print (students[0])
# print (students[1])
#for student in students:
    #print (student["name"], student["house"], student ["patronus"], sep = " | ")
# see the output .. it only prints out the values and not the keys .. how do I print the keys and the values? 
# the class did not address this
# 
# print ("#")
# print ("#")  
# print ("#")  
# this will print the hash character three times on top of eachother
# this code below does the same thing 
# for _ in range (3):
#     print("#")
#  Now this change this
# def main():
#     print_column (3)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# main()
# this prints a square of 4 X 4 .. this is my technique .. 
# def main():
#     print_row (4)

# def print_row (width):
#     for _ in range (width):
#         print ("?" * width)

# main ()

# this is what the instructor taught to do the same thing. 
# It seems much too complicated- I did mine with much less code.

def main ():
    print_square (3)

def print_square (size):
   for i in range (size):
        for j in range (size):
            print ("?", end = "")
        print ()

main ()






    





    