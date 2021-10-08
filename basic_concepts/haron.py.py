'''write a program to caln the area of 
triangle using haron's formula'''
a=int(input("enter the 1st side "))
b=int(input("enter the 2nd side "))
c=int(input("enter the 3rd side "))
s=(a+b+c)/2
if(((a+b)>c) and ((b+c)>a) and ((a+c)>b)):
    area=((s*(s-a)*(s-b)*(s-c))**0.5)
    print("The Area is:",area)
else:
    print("invalid triangle")