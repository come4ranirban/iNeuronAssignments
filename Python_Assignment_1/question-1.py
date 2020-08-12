'''ASSIGNMENT-1'''
temp = ''
for i in range(2000,3201):
    if((i%7==0) and (i%5!=0)):
        temp = temp+str(i)+','
print("no.s which are multiple of 7 but not of 5 ->", temp)        
