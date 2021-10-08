'''Write a program to print the table'''
a=int(input("enter the number : "))
n=int(input('enter the end point of the table : '))
for i in range(0,n+1):
    x=a*i
    print(str(a)+'*'+str(i)+'='+str(x))