''' Calculating income'''
income=int(input("ENTER THE INCOME:"))

if(income<=150000):
    tax=income*0
    print("no tax applied")
    total=income-tax
    print("total income=",total)
    
elif(income>150000 and income<=300000):
    tax=income*0.1
    print("tax applied=",tax)
    total=income-tax
    print("total income=",total)
       
elif(income>350000 and income<=500000):
    tax=income*0.2
    print("tax applied=",tax)
    total=income-tax
    print("total income=",total)
      
else:
    tax=income*0.3
    print("tax applied=",tax)
    total=income-tax
    print("total income=",total)
     