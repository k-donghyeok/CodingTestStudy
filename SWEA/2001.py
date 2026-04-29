T= int(input())


for test in range(1,T+1):
    n,m=map(int,input().split())
    array=[]
    for i in range(n):
        array.append(list(map(int,input().split())))


dx=[0,0,-1,1] # 상 하 좌 우   
dy=[-1,1,0,0]


result=[]
for i in range(n-m+1):
    for j in range(n-m+1):
        sum=0
        for k in range(i,i+m):
            for l in range(j,j+m):
                sum+=array[k][l]
        result.append(sum)   

print(f"#{test} {max(result)}")