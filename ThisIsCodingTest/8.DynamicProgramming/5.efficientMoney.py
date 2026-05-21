n,m = map(int,input().split())

array=[]
for i in range(n):
    array.append(input().rstrip())

#print(array)
dp=[0 for _ in range(m+1)]
def dfs(current):

    if(dp[current]!=0):
        return dp[current]

    if(current==m):
        return 0

    result = 999999

    for i in range(len(array)):
        nx=current+int(array[i])

        #print(nx,depth+1)
        if(nx<=m):
            result=min(result,dfs(nx)+1)

    dp[current]=result
    return result

result=dfs(0)
if(result==999999):
    print(-1)
else:
    print(result)