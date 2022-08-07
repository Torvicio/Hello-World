# Loops and iteration

# 1. for loop -- iteration
# for each item in some collection, do ssome stuff

# Your list
programs_to_write = [
    "slightly better bash script",
    "web crawler",
    "port scanner",
    "web application",
    "cloud provisioning tool",
    ]

# Basic From - INDENTATION is key! 
# for  program_name in programs_to_write:
#     print ("I'm going to write a", program_name) #capitalize
        
# print ("\n ... We're done!")
# print ("but it's not all fun -- the loop variable --",program_name, "still exists")

# #  while loop -- a traditional loop
# something__true = True
# while (something_true):
#     print ("Welcome to my game!")
#     print ("Going through the loop")
    
#     # possiblly """  """make something_true = Fsles
#     something_true = False
# print("We are done. something_true is now ... um err ", something_true)

# Print Meow some number of times with input
#Break into functions Main - Meow function and Get Input function

def main():
    number = get_number()
    meow(number)

def get_number():
    n = input("Give me a number greater than 0: ")
    return n

def meow ():
    print ("Meow")

main()
