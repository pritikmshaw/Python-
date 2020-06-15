'''print FIZZ if I is divisible by 3 or print BUZZ
 if I is divisible by 5 or print FIZZBUZZ  if I
 is divisible by both 3 and 5. Where I is in the
 range of 1 to 500'''
for i in range(1,500):
    if(i%3==0 and i%5==0):
        print('FIZZBUZZ')
    elif(i%5==0):
        print('buzz')
    else:
        print('fizz')