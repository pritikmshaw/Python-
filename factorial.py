'''write a program to print the factorial of the
 given numbers'''
n=int(input("Enter a no"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of "+str(n)+" is : "+str(fact))