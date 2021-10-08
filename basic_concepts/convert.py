'''write a program to convert binary 
number to decimal number'''
no=input("Enter the binary no")
flag=0
dec=0
for i in range(len(no)-1,-1,-1):
    a=int(no[i])
    dec=dec+(a*(2**flag))
    flag+=1
print("The Decimal Value is : ",dec)