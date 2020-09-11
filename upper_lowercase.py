# check wheather the character is a upper case lower case or special character 
#If the ASCII value of the character is between 65 and 90, print "Upper".
#If the ASCII value of the character is between 97 and 122, print "Lower".
#If the ASCII value of the character is between 48 and 57, print "Number".
#Else, print "Symbol".

ch = input("character: ")
if(ord(ch) >= 65 and  ord(ch) <= 90):
    print (" upper")
elif (ord(ch) >=97 and  ord(ch) <= 122):
    print("lower")
elif (ord(ch) >=48 and  ord(ch) <= 57):
    print("number")
else:
    print("symbol")