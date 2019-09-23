############ Question-1 ############
a = eval(input("Enter a number:"))
print (a)
if(a%3 == 0):
    print("Consultadd")
if(a%5 == 0):
    print("Python Training")
if(a%3 == 0 and a%5 == 0):
    print("Consultadd Python Training")
############ Question-2 #############
print("Choose following")
print(" For Addition enter-1 \n For Subtraction enter-2 \n For Division enter-3 \n For Multiplication enter-4 \n For Average enter-5")
operation = eval(input())
if (operation == 1 or operation == 2 or operation == 3 or operation == 4):
    first = eval(input("Enter num1:"))
    second = eval(input("Enter num2:"))
    if (operation == 1):
        print("ADDITION")
        b = first+second
        if (b >= 0):
            print (b)
        else:
            print("Oops option X(", operation,") is returning the negative number")
    elif (operation == 2):
        print("Subtraction")
        b = first-second
        if (b >= 0):
            print (b)
        else:
            print("Oops option X(", operation,") is returning the negative number")
    elif (operation == 3):
        print("Division")
        b = first/second
        if (b >= 0):
            print (b)
        else:
            print("Oops option X(", operation,") is returning the negative number")
    elif (operation == 4):
        print("Multiplication")
        b = first*second
        if (b >= 0):
            print (b)
        else:
            print("Oops option X(", operation,") is returning the negative number")
elif (operation == 5):
    first = eval(input("Enter num1:"))
    second = eval(input("Enter num2:"))
    first1 = eval(input("Enter num3:"))
    second2 = eval(input("Enter num4:"))
    print("Average")
    b = (first+second+first1+second2)/4
    if (b >= 0):
        print (b)
    else:
        print("Oops option X(", operation,") is returning the negative number")
else:
    print("invalid")
############ Question-3 #############
a = 10
b = 20
c = 30
avg = (a+b+c)/3
print("avg = ", avg)
if(avg > a and avg > b and avg > c):
    print("avg is higher than a,b,c")
elif (avg > a and avg > b):
    print("avg is higher than a,b,c")
elif (avg > a and avg > c):
    print("avg is higher than a,c")
elif(avg > b and avg > c):
    print("avg is higher than b,c")
elif (avg > a):
    print("avg is just higher than a")
elif (avg > b):
    print("avg is just higher than b")
elif (avg > c):
    print("avg is just higher than c")
else:
    print(avg)
############ Question-4 #############
i = 0
while (i >= 0):
    d = eval(input("Enter any value:"))
    if (d <= 0):
        break
    else:
        print("Good going")
        continue
print("Its Over")
############ Question-5 #############
numbers = []
for x in range(2000, 3200):
    if(x%7 == 0 and x%5 != 0 ):
        numbers.append(str(x))
print(','.join(numbers))
############ Question-6 #############
### part-a ###
#x = 123
#    for i in x: #unexpected indentation
#        print(i)
### part-b ###
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:           #isnt gonna execute as its not in write indent.
    print("error")
### part-c ###
count = 0 
while True:
    print(count)
    count += 1
    if count >=5:
        break  #Break is supposed to be with small b
############ Question-7 #############