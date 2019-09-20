######## Question-1############
a,b,c = 1, 10.8, 'Assignment'
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))
######### Question-2 ###########
d = complex(a,b)
print(d)
print(type(d))
d = int(d.real)
print(d)
print(type(d))
######### Question-3 ###########
## with third var ##
result = b
b = a
a = result
print(a,b)
## without third var ##
a,b = b,a
print(a,b)
######### Question-4 ###########
## python 2.x ##
print raw_input('Assignment 1 Question 4 part:') ## Error when run with python 3
## python 3.x ##
print(input('Assignment 1 Question 4 part:')) ## runs fine with both python 2 ,3 
######### Question-5 ###########
## part a ##
print('Enter any 2 numbers in between 1-10:')
e = eval(input('number1:'))
f = eval(input('number2:'))
z = e+f
print("z=",z)
## part b ##
result = print('result = ', z + 30)
######### Question-6 ###########
print('The input value data type is : ')
print(type(e))
######### Question-7 ###########
camelCaseLadder_CaseUPPERCASE = 20
######### Question-8 ###########
print('data type of a is:',type(a))
print('value of a = ',a)
a = str(a)
print('Now data type of a is:',type(a))
print('Now value of a = ',a)
a = float(a)
print('Now data type of a is:',type(a))
print('Now value of a = ',a) # The datatype changes but value remains same exept it changes it representation that is if converted to float from integer it will change from 1 = 1.0
