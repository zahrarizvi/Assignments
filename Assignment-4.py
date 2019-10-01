############# Question-1 #############
print("already done in assignment-3 question-1")
############# Question-2 #############
print("already done in assignment-3 question-2")
############# Question-3 #############
x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
##part-a##
print(x[5][:4])
##part-b##
print(x[6:8])
##part-c##
print(x[::2])
##part-d##
#method-1#
print(x[::-1])
#method-2#
#x.reverse() #this will change the orignal list in reverse order
#print(x)
##part-e##
print(x[5][5][0])
##part-f##
print(x[9:-9])
############# Question-4 #############
print(range(1000)) #in python2.x this will print out 1000 values on the terminal
#in python 3.x range will work same as xrange in python2.x but xrange(keyword) doesnt exist in python 3.x
#print(xrange(1000)) #in python2.x this will only allocate 1000 memory spaces and will print out range(0,1000)
############# Question-5 #############
#Tuples are better than list beacuse , 
# Tuples are heterogenous data structures that is they are more organized more defined than list,
# Tuples have structure where as list has order.
# If you time your python code using then you will know tuple works faster than list.
# Tuples are immutable that is the data in tuple is accesable but not changeble. 
# This gives security to your data.
############# Question-6 #############
for i in range(1,100):
    if (i%3 == 0 and i%2==0):
        print (i)
    else:
        pass
############# Question-7 #############
string = input("Enter a string:\n")
string = string[::-1]
print("reversed string\n", string)
vowel = ['a','e','i','o','u']
for i in range(len(string)):
        if string[i] in vowel:
            print(string[i],i)
############# Question-8 #############
name = "Hello my name is abcde"
word = name.split()
print(word)
for i in word:
    if len(i)%2==0:
        print(i)
############# Question-9 #############
x = [1,2,3,4,5,6,7,8,9,-1]
for i in range(len(x)):
    for j in range(i+1 , len(x)):
        if x[i]+x[j] == 8:
            print("(",x[i],",",x[j],")")
############# Question-10 #############
even_list = [0,2,4,6,8,10]
odd_list = [1,3,5,7,9,11]
i = 'Y'
e = 0
o = 0
#user_input = eval(input("Enter data in the range of (1,150)"))
while i == 'Y' and (e<5 or o<5):
    user_input = eval(input("Please Enter data in the range of (1,150)"))
    if user_input in range(1,150):
        if e<5 and o<5:
            if user_input%2 == 0 and e < 5:
                even_list.append(user_input)
                print(even_list)
                e+=1
                print(e)
                i = input("Do you wanna enter data again in range (1,150)(Y/N)?")
            elif user_input%2!=0 and o < 5:
                odd_list.append(user_input)
                print(odd_list)
                o+=1
                print(o)
                i = input("Do you wanna enter data again in range (1,150)(Y/N)?")
        else:
            print("Already added 5 inputs in both lists")
            break
    else:
        i = input("Do you want to enter data again in range (1,150)(Y/N)?")
    
    
############# Question-11 #############
alphanumeric = "12abcbacbaba34ab"
new = dict()
for i in range(len(alphanumeric)):
    if (alphanumeric[i].isalpha()):
        if alphanumeric[i] not in new:
            new[alphanumeric[i]] = 1
        else:
            new[alphanumeric[i]] = new[alphanumeric[i]]+1
    else:
        pass
for i in new.keys():
    print(i, "=", new[i])
############# Question-12 #############
tuple_list = (1,2,3,4,5,6,7,8,9,10)
even = []
for i in tuple_list:
    if i % 2 == 0:
        even.append(i)
print(tuple(even))