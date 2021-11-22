
#### still working on it













import math

#FirstVal = input("Please enter the first value: ")
#SecondVal = input("Please enter the second value: ")

##Pyt= math.sqrt(a**2+b**2)

def neg(a,b):
    if a<0 and b>0:
        a = abs(a)
        print(a, b)
    elif a>0 and b<0:
        b= abs(b)
        print(a, b)
    else:
        a= abs(a)
        b= abs(b)
        print(a, b)
        

def isCompl(a,b):
    if (type(a) == complex and type(b) == int):
        a= a.real
        print(a,b)
    elif (type(a) == int and type(b) == complex):
        b= b.real
        print(a,b)
    else:
        a=a.real
        b=b.real
        print(a,b)



def Pythagore(a, b, c=0):
    if (type(a) == str or type(b) == str):
        print("[!] The entered value's type is Str please enter a valid value")
        if (type(a) == str and type(b)== int):
            a = int(input("Please enter a number: "))
            c = math.sqrt(a**2+b**2)
            print('The result is:', c)
        elif (type(a) == int and type(b) == str):
            b= int( input("Please enter a number: "))
            c = math.sqrt(a**2+b**2)
            print('The result is:', c)
        elif (type(a) == complex or type(b) == complex):
            isCompl(a,b)
            c = math.sqrt(a**2+b**2)
            print('The result is:', c)
        elif (a<0 or b<0):
            neg(a,b)
            c = math.sqrt(a**2+b**2)
            print('The result is:', c)
    
    

Pythagore(7, -9)
    
