n,m = map(int,input().split())

array=[]
for i in range(n):
    array.append(int(input()))

dp=[0 for i in range(1,10001)]

for i in range(len(array)):
    dp[array[i]-1]=1
    

j=max(array)+1
while(j<=m):
        for i in array:
            if(j-i>=min(array)):
                dp[j]=min(dp[j-i]+1,dp[j])+1
                j+=1
            
   
print(dp[m])