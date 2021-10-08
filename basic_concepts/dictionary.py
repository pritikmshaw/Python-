'''write a program to create a dictionary GROCERY 
contain item names and price of 5 items. Then find
 total bill to be paid. Print iten with price and 
 total bill amount.'''
D={' item1 ':10,' item2 ':20,' item3 ':30,' item4 ':40,' item5 ':50}
sum=0
print(D)
sum=sum+D[' item1 ']
sum=sum+D[' item2 ']
sum=sum+D[' item3 ']
sum=sum+D[' item4 ']
sum=sum+D[' item5 ']
print('Total = '+str(sum))