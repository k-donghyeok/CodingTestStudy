# 4:47
# 5:36

# 음 배열의 모든 열을 일단 방문을 해야하고 방문 순서는 랜덤
# 모든경우의수 지금 한 선택이 최선이 아닐수있음
# 근데 선택한다 안한다로 안되는게 0 1 2 3 이렇게 순서대로 가는게아니라
# 0 2 3 1 이렇게 이동이 가능하네 순서가 있고 모든 경우의수
# 0부터 시작해서 0으로 끝나야하고 순서가 있을때 모든 경우의수
# 0 1 2 3 0    0 1 3 2 0   0 2 1 3 0    0 2 3 1 0
from collections import deque
T=int(input())

for test_case in range(1,1+T):
    n=int(input())
    array=[]
    for i in range(n):
        array.append(input().split())
    result=99999
    visited=[0 for _ in range(n)]

    def dfs(start,end,sum,count):
        global result
        if(count==n):
            sum=sum+int(array[end][0])
            result=min(result,sum)
            return
        for i in range(1,n):
            if(visited[i]==0):
                visited[i]=1
                dfs(end,i,sum+int(array[end][i]),count+1)
                visited[i]=0


    dfs(0,0,0,1)
    print(f'#{test_case} {result}')