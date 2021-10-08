'''formula for finding the roots
 of the quaratic equation ax2+bxc '''
import cmath
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
d=(b*b)-4*a*c
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print("sol 1:",sol1)
print("sol 2:",sol2)