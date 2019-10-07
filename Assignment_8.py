############### Question-1 ###############
import math
class squareroot:
    def __init__(self,c,H,D):
        self.c = c
        self.H = H
        self.D = D
    def sqrt(self):
        for i in self.D:
            print(math.sqrt((2*self.c*int(i)/self.H)))

d = input("Please enter digits in comma seperated way: \n")
D = [D for D in d.split(',')]
obj = squareroot(50,30,D)
obj.sqrt()
############### Question-2 ###############
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self)
        self.length = length
    def area(self):
        return self.length*self.length
Squareobject = Square(3)
print("Length = ",Squareobject.area())
############### Question-3 ###############
class sumzero:
    def sum(self,input_array):
        self.input_array, result, i = sorted(input_array), [], 0
        while i < len(input_array) - 2:
            j, k = i + 1, len(input_array) - 1
            while j < k:
                if input_array[i] + input_array[j] + input_array[k] < 0:
                    j += 1
                elif input_array[i] + input_array[j] + input_array[k] > 0:
                    k -= 1
                else:
                    result.append([input_array[i], input_array[j], input_array[k]])
                    j, k = j + 1, k - 1
                    while j < k and input_array[j] == input_array[j - 1]:
                        j += 1
                    while j < k and input_array[k] == input_array[k + 1]:
                        k -= 1
            i += 1
            while i < len(input_array) - 2 and input_array[i] == input_array[i - 1]:
                i += 1
        return result
input_array = [-25,-10,-7,-3,2,4,8,10]
print(sumzero().sum(input_array))
############### Question-4 ###############
## part a ##
'''class Test:
    def __init__(self): # def needs to be under the class Test indentation to run def __init__(self).SYNTAX ERROR
        self.x = 0
class Derived_Test(Test):
    def __init__(self): # def needs to be under the class Derived_Test(Test) indentation to run def __init__(self).SYNTAX ERROR
        self.y = 1
def main(): # def needs to be under the class Derived_Test(Test) indentation to run def main().SYNTAX ERROR
    b = Derived_Test()
    print(b.x,b.y) # x attribute thats defined in init of parent class doesnt not take x as an attribute.ATTRIBUTE ERROR
main() 
## part b ##
class A:
    def __init__(self, x= 1): # def needs to be under the class A indentation to run def __init__(self,x=1).SYNTAX ERROR
        self.x = x
class der(A): 
    def __init__(self,y = 2): # def needs to be under the class der(A) indentation to run def __init__(self,y=2).SYNTAX ERROR
        super().__init__() 
        self.y = y
def main(): # def needs to be under the class der(A) indentation to run def main().SYNTAX ERROR
    obj = der()
    print(obj.x, obj.y)
main()#) #extra closing bracket.SYNTAX ERROR 
 If no error then output will be '1 2' 
## part c ##
class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1
def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)
main() ## result '3 1' No Error. '''
## part d ##
class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)

    def multiply(self, i):
        self.i = 4 * i#; # unnecesarry semi colon
class B(A):
    def __init__(self):
        super().__init__()

    def multiply(self, i):
        self.i = 2 * i#; # unnecesarry semi colon
obj = B() # result '30'. No Error Object of B() was called so when reached to init function 
          # of A (as supper's init is called in child's init) ,multiply func of B was called giving 2*15 = 30
############### Question-5 ###############
class Time():
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
    def addTime(time1,time2):
        t3 = Time(0,0)
        if time1.minutes+time2.minutes > 60:
            t3.hours = int((time1.minutes+time2.minutes))/60
        t3.hours = t3.hours+time1.hours+time2.hours
        t3.minutes = int(time1.minutes+time2.minutes)-int(int((time1.minutes+time2.minutes)/60)*60)
        print(time1.hours,"hour and",time1.minutes,"min + ",time2.hours,"hrs",time2.minutes,\
              "min =",t3.hours,"hours",t3.minutes,"minutes")
        return t3
    def displayTime(self):
        print("Time is ", self.hours,"hrs and ", self.minutes,"minutes")
    def DisplayMinute(self):
        return self.hours*60+self.minutes
obj = Time(1,20)
obj2 = Time(2,30)
obj3 = Time.addTime(obj,obj2)
print(obj3.DisplayMinute(),'minutes')
obj3.displayTime()
############### Question-6 ###############
class person:
    def __init__(self,age):
        if age < 0:
            print("Age not valid,setting age to 0")
            self.age = 0
        else:
            self.age = age
    def yearPasses(self):
        return self.age + 1
    def amIOld(self):
        if self.age <= 12 and self.age > 0:
            print("You are young")
        elif self.age <= 13 and self.age > 0:
            print("You are a teenager")
        elif self.age >= 20 and self.age > 0:
            print("You are old")
        else:
            pass
Age = person(eval(input("Enter your age: ")))
Age.amIOld()
print(Age.yearPasses())