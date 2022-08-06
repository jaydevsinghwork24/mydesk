def addition(a,b):
    print(a+b)
def subtraction(a,b):
    print(a-b)
def multiplication(a,b):
    print(a*b)
def division(a,b):
    print(a/b)
x= int(input("choose no for calculation like multiplication: 1, addition: 2, subtraction: 3, division: 4"))
if x==1:
    a=int(input("enter the first no"))
    b=int(input("enter the second no"))
    multiplication(a,b)
elif x==2:
    a = int(input("enter the first no"))
    b = int(input("enter the second no"))
    addition(a, b)
elif x==3:
    a = int(input("enter the first no"))
    b = int(input("enter the second no"))
    subtraction(a, b)
else:
    a = int(input("enter the first no"))
    b = int(input("enter the second no"))
    division(a, b)