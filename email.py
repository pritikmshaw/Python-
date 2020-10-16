name=[]
domain=[]
for i in range(5):
    email=input("enter the email address:")
    for j in range(len(email)):
        if(email[j]=='@'):
            name.append(email[:j])
            domain.append(email[j+1:])
print("names:",tuple(name))
print("domain:",tuple(domain))
