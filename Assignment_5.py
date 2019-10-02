############# Question-1 #############
def reverse(string):
    return ''.join(reversed(string))
print(reverse("1234abcd"))
############# Question-2 #############
def upperlowercase(string):
    count_uppercase = count_lowercase = 0
    for i in string:
        if i.isupper():
            count_uppercase+=1
        elif i.islower():
            count_lowercase+=1
    print("No. of Upper case characters:",count_uppercase)
    print("No. of lower case characters:",count_lowercase)
upperlowercase("AssIgnMent5Q2")
############# Question-3 #############
def unique_elements(lists):
    new_set = set(lists)
    new_list = list(new_set)
    return new_list
print(unique_elements([1,2,3,4,4,5,6,6,6,6,5,5,5,8,8,7,7,5,4,3,2,2,3,1]))
############# Question-4 #############
def hyphen_seperated(string):
    new_list = string.split('-')
    new_list.sort()
    sorted_string = '-'.join(new_list)
    return sorted_string
print(hyphen_seperated("Syeda-Zahra-Ali-Rizvi"))
############# Question-5 #############
def iscapital():
    sequenceofstring = []
    while True:
        l = input("enter line")
        if l:
            sequenceofstring.append(l.upper())
        else:
            break
    for l in sequenceofstring:
        print(l)
iscapital()
############# Question-6 #############
def sum_string(s1,s2):
    return int(s1)+int(s2)
s1 = input("Enter number 1")
s2 = input("Enter number 2")
print(sum_string(s1,s2))
############# Question-7 #############
def max_string(string1,string2):
    if max(len(string1),len(string2)) > len(string1):
        print(string2,"length =\b",len(string2))
    elif max(len(string1),len(string2)) < len(string1):
        print(string1,"length =\b",len(string1))
    elif len(string1) == len(string2):
        print(string1)
        print(string2)
    else:
        pass
string1 = input("enter any string1:\b ")
string2 = input("enter any string2:\b ")
max_string(string1,string2)
############# Question-8 #############
def tuple_square():
    square = []
    for i in range(1,21):
        square.append(i*i)
    print(tuple(square))
tuple_square()
############# Question-9 #############
def showNumbers(limit):
    for i in range(limit):
        if i%2 == 0:
            print(i,"EVEN")
        else:
            print(i,"ODD")
limit = eval(input("Enter Limit: \b "))
showNumbers(limit)
############# Question-10 #############
evenNumbers = list(filter(lambda x:x%2==0 ,range(1,21)))
print(evenNumbers)
############# Question-11 #############
numbers = list(range(1,11))
squareOfEvenNumbers = list(map(lambda x:x*2, filter(lambda x:x%2==0, numbers)))
print(squareOfEvenNumbers)
############# Question-12 #############
def compute():
    return 5/0
try:
    compute()
except ZeroDivisionError:
    print("Error, Cant divide by zero")
############# Question-13 #############
import functools ,operator
l = [[1,2,3],[4,5],[6,7,8]]
flatten = functools.reduce(operator.add,l)
print(flatten)
############# Question-14 #############
### part-a ###
def foo():
    try:
        return 1
    finally:
        return 2
    k = foo()
    print(k) #isnt going to run as no where called
### part-b ###
#def a():
#    try:
#        #f(x,4) #Name-Error as f is not defined
#    finally:
#        print("after f")
#    print('after f?')
#a()