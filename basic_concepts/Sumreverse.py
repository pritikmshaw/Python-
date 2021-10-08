'''given a list A of N numbers, you have to write
 a program which prints the sum of the elements 
of the array A with the corresponding elements of
 the reverse of array A. if the array A has 
 elements [1,2,3] then reverse of the array A
 will be [3,2,1] and the resultant array should
 be [4,4,4]'''
a=[1,2,3]
b=[0,0,0]
c=[0,0,0]
print(a)
b[0]=a[2]
b[1]=a[1]
b[2]=a[0]
print(b)
c[0]=a[0]+b[0]
c[1]=a[1]+b[1]
c[2]=a[2]+b[2]
print(c)