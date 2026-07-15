#writing a program to print get length
"""
print("enter the length")
length = int(input("Length: "))
width = int(input("width: "))
Area=length*width
print("Area" , Area)
"""
#write to print it is even or odd
"""

print("enter the number")

number = int(input("number: "))
if number%2==0:
    print("it is even")
else:
    print("it is not even")
    """

#input two number and get their avg

""""
a=int(input("a: "))
b=int(input("b: "))
avg=int((a + b) / 2)
print(avg)
"""
#input two number and greator in it
"""
print("ENter number 1")

a=int(input("a: "))
print("ENter number 2")

b=int(input("b: "))

if a>b:
    print("a is greator than b")
elif a<b:
        print("b is greator than a")
        """
# str="Python is a powerful and easy-to-learn programming language used for web development, data science, artificial intelligence, automation, game development, and much more. It is loved by beginners and professionals because of its simple syntax, huge community support, and wide range of libraries that make complex tasks much easier"
# print(str.replace("and","or"))
# print(str.endswith("l"))
# print(str[-1:-4:-1])


#entering name and checking its length
"""
print("enter your name")
user=input("name:")
print(len(user))
print(user.find('a'))
"""
#assigning grade to student according to marks
"""
print("if you want to know to grade enter your marks out of hundred")
marks=1
marks=int(input("marks:"))
if marks >= 100 :
    print("marks should be less then 100") 
    
elif marks >= 90:
    print("A Grade conngrats") 
elif marks>80 and marks<90:
    print("B Grade conngrats") 
elif marks>70 and marks<80:
    print("C Grade conngrats") 
elif marks>70:
    print("D Grade conngrats") 
    """
    #making table of any number n
""" 
print("give me a number to print table")
count=1
number=int(input("number :"))
while count<=10:
    print(number,"*",count,"=",count*number)
    count+=1
    """ 
# print("give me a number to print table")
"""
count=1
print(count**count)
while count<=10:
    print(count**2)
    count+=1
    """
# thistuple=(2,3,4,4,5,5,5)
# for el in thistuple:
#     if el==3:
#         print("finded",el,'at index',thistuple.index(el))
#     print(el)
'''
input=int(input("num:"))
factorial=1
for i in range(1,input):
        print("step")
        factorial *=input  
        input-=1
        
    
        print("factorial",factorial)
        '''
'''
def my_func(list):
    length= len(list)
    return length

print(my_func([1,3,4,5,6,78]))

'''
"""
def factorial(fac):
    factorial=1
    for i in range(1,fac):
        print("step")
        factorial *=fac  
        fac-=1
    
    print("factorial",factorial)
    print("factorial", fac)


factorial(3)
"""
"""
def func_covertiontousd(pkr):
    print("working")
    usd=int(pkr*0.0036)
    print(usd)
    return usd

func_covertiontousd(6000)


grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade) 
"""

"""

def sumofnumtural(n):
    if(n==0):
        return 
    print(n)
    sumofnumtural(n-1)
     

    
    
    
    
print(sumofnumtural(10))
    """
"""
with open("bilal.txt", "r") as file1:
  file1=file1.read()
  new=file1.replace("java","python")
with open("bilal.txt","w") as file2:
    str= file2.write(new)
with open("bilal.txt", "r") as file1:
  file1=file1.read()
  print(file1)
      """ 
"""
def checkwordline(word):
    count=0
    line=0
    with open("bilal.txt", "r") as file1:
        line1=file1.readline() 
        linecheck=line1.count(word)
        count+=linecheck 
        if linecheck>0:
            line=1
        print("finded" ,word,"in","line",line,"for",count,"time")
    print("letsgo")
      
      
checkwordline("python")      
"""
# class Student:
#     def __init__(self,fullname,english,urdu,math):
#         self.fullname=fullname
#         self.english=english
#         self.urdu=urdu
#         self.math=math
#         print("adding user name")
#     def hello(self,):
#             print(self.fullname)
#             math=int(self.math)
#             english=int(self.english)
#             urdu=int(self.urdu)
#             print(int((math+english+urdu)//3))
            
            
# student=Student("khrwehekri3",20,30,50)
# student.hello()
# class Bankbilal:
#     def __init__(self,balance):
#         self.balance=balance
#         print("your blance is updated")
#     def credit(self,addition):
#         self.addition=addition
#         self.balance+=addition
#         print(self.balance)
#     def debit(self,subtraction):
#         self.addition=subtraction
#         self.balance-=subtraction
#         print(self.balance)

# bank=Bankbilal(20000)
# del bank.credit()
# bank.credit(2000)
# bank.debit(2000)
class makingemploye:
    def __init__(self,name,salary,role,experience):
        self.name=name
        self.salary=salary
        self.role=role
        self.experience=experience
    def showdetails(self):
        print("yourname is",self.name,"your role is ",self.role)
        
        
        
data=makingemploye("bilal","120000$","FullStack Ai engineer","5 Years")
print(data.showdetails())
        
