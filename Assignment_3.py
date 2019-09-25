############# Question-1 #############
a = [1,2,'Syeda','Ali',1+3j,1.2,3.2,4.5,2+4j,'training']
print(a)
############# Question-2 #############
b = [1,2,3,4,5]
print(b[:3]) 
print(b[:])
print(b[2:4])
print(b[1:])
print(b[::2])
############# Question-3 #############
print("List = ",b)
add = 0
mul = 1
for i in range(len(b)):
    add = add + b[i]
    mul = mul * b[i]
print("Addition of the given list:",add)
print("Multiplication of the given list:",mul)
############# Question-4 #############
print("List = ",b)
print(max(b))
print(min(b))
############# Question-5 #############
print("List = ",b)
new = []
for j in b:
    if (j % 2 == 0):
        new.append(j)
        b.remove(j)
print("exsisting list after deleting evens  =", b)
print("new even list = ",new)
############# Question-6 #############
lists = []
for i in range(1,30):
    lists.append(i*i)
print(lists[:5])
print(lists[-5:])
############# Question-7 #############
sample_data1 = [1,3,5,7,9,10]
sample_data2 = [2,4,6,8]
sample_data1.pop(-1)
sample_data1.extend(sample_data2)
print("Expected output:", sample_data1)
############# Question-8 #############
a = {1:10,2:20}
b = {3:30,4:40}
c = {**a , **b}
#c = a.update(b) # returns none beacuse of command query seperations
#print("Expected output:", dict(b , **a)) #works with python2
print("Expected output:",c)
############# Question-9 #############
output = dict()
for i in range(1,5+1):
    output[i]=i*i
print("Expected output:",output)
############# Question-10 #############
numbers = input("Enter comma seperated numbers")
list = numbers.split(",")
print(list)
print(tuple(list))
