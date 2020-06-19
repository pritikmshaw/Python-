'''write a program to define the list of moods in 
three different list [sad,happy,neutral]. Take 
input one word and print which mood it belongs 
too.'''
happy=["laugh","fun","enjoy"]
sad=["cry","depressed","bad"]
neutral=["alu","cu","cpu"]
x=input("enter word")
for i in range (0,3):
    if x==sad[i]:
        print("sad")
    elif x==happy[i]:
        print("happy")
    elif x==neutral[i]:
        print("neutral")