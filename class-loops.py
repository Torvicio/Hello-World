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
# Dictionanry -  {}
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

for student in students:
    # print(students [student])
    print (student,":", students[student])
    # or 
    print (student, students [student],sep=":")
    

# above prints out the value associated with the item in []













    





    