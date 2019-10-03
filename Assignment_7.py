############# Question-1 #############
def throwSyntaxError():
    try:
        eval('x===x')
    except SyntaxError:
        print("It was a Syntax Error")
throwSyntaxError()
############# Question-2 #############
from sys import argv
nameofprogram, filename = argv
print("Name of the program is:", nameofprogram)
print("Name of the file is:",filename)
while True:
    try:
        fh = open(filename)
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        print('hello the name entered is wrong, Please provide correct name')
        try_again = input("Do you want to try again!!!Write the correct name if you want(Y/N)")
        if try_again=='Y':
            filename=input("Please enter the name of file correctly \t")
        else:
            break
############# Question-3 #############
try:
    number = eval(input("Please enter a number: "))
    if len(str(number))!= 4:
        raise(ValueError)
except ValueError:
    print("Please length is too short/long!!! Please provide only four digits")
############# Question-4 #############
UserEmail = input("UserEmail = ")
password = input("Password = ")
Re_password = input("Re-type Password = ")
count = 1
try:
    while count < 3:
        if Re_password != password:
            print("Password didnt match!! Try Again \n")
            Re_password = input("Re-type Password = ")
            count+=1
        else:
            break
except:
    print("Cant try more than 3 times, User Blocked")
############# Question-5 #############
############# Question-6 #############
#write_file = open('doc.txt','w')
#write_file.write("Hello I am a file\nWhere you need to return the data string\nWhich is of even length\nMake sure you return the content in\nThe same link as it is present.")
open_file = open('doc.txt')
for i in open_file.readlines():
    if len(i)%2==0:
        print(len(i),"=",i)
open_file.close()