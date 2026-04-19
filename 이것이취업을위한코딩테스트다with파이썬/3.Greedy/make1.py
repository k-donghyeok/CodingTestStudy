number,k = map(int,input().split())
count=0
while(number !=1):
    if(number%k==0):
        number=number//k
        count+=1
        continue
    elif(number%k!=0):
        number-=1
        count+=1

print(count)