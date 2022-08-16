# Python3 program to convert string
# from camel case to snake case
 
def change_case(file_name):
    res = [file_name[0].lower()]
    for c in file_name[1:]:
        if c in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
     
    return "".join(res)
     
# Driver code
file_name = input("Enter your file name:" )
print(change_case(file_name))