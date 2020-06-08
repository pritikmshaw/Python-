'''how to find the greatest number amgong 3 numbers '''
a=input("enter a:")
b=input("enter b:")
c=input("enter c:")
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)