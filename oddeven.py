'''write a program to print all the numbers from
 m-n thereby classifying them as even or odd'''
m=int(input('upper case'))
n=int(input('lower case'))
for i in range(m,n+1):
    if(i%2==0):
        print(str(i)+'--even')
    else:
        print(str(i)+'--odd')