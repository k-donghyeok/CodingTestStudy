T = int(input())

for test_case in range(1,T+1):
    n=int(input())

    visited=[0]*n

    result=0

    def check(col):
        if(visited[col]==1):
            return false

        if()


    def dfs(col):
        global result
        if(col==n):
            result+=1
            return
        if(check(col)):
            visited[col]=1
            dfs(col+1)