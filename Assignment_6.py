############# Question-1 #############
print(list(filter(lambda x:(x%7==0 and x%3!=0),range(100))))
#print([x for x in range(100) if (x%7==0 and x%3!=0)])
############# Question-2 #############
def multiple(x):
    x = x*x
    return x
print(list(map(multiple,range(10))))
############# Question-3 #############
print([i for i in "SyedAzahraALIRizVi" if i.isupper()==True])
############# Question-4 #############
Student = ['Smit','Jaya','Rayyan']
capital = ['CSE','Networking','Operating System']
### Using zip function ###
dictionary_zip = dict(zip(Student,capital))
print(dictionary_zip)
### Dictonary Comprehension ###
print({Student[i]:capital[i] for i in range(len(Student))})
############# Question-5 #############
##Yield##
''' Yeild statement terminates the function's itteration and return the value but retains the previous
value to resume the function where it left off.'''
##next##
''' Next is mostly used with files when used as an iter() function or with loops. It gives the next line input or 
EOF if is at the end. '''
##Generators##
'''A function that contains one or more than one yeild statements is then called generators.'''
############# Question-6 #############
def reverse_gen(string):
    yield string[::-1]
print(list(reverse_gen("hello")))
def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1,-1,-1):
        yield my_str[i]
for char in rev_str("Consultadd Training"):
     print(char)
############# Question-7 #############
''' Decorators is a function that calls another function in it to extend the behaviour 
of that other function without permanently modifying it. '''
#example#
def hello_decorato(func):
    def inner(a,b):
        print("before execution")
        returned_value = func(a,b)
        print("after Execution")
        return returned_value
    return inner
@hello_decorato
def sum_two_numbers(a,b):
    print("inside the function")
    return a+b
a,b = 2,2
print("sum=",sum_two_numbers(a,b)) 
############# Question-8 #############
'''Front end is the part of application or website which is accessible to user(user interface)
 for-example buttons,programs, websites, and other features, it is the layer above the backend part of a software.
 This concept is mostly used in software, website and application development. 
 For designs and Graphic deployment HTML,CSS,Javascript are used. 
 SEO also comes in handy for front end.
 Testing of a software is also considered as front end as its used to check the accessibility and usability of a software,website or application.
 Version Control like GIT are also considered as front end
 Browser compatibility, development tools
 '''