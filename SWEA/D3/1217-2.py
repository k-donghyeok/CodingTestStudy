# 8:20

for _ in range(10):
    test_case=int(input())

    n,m =map(int,input().split())
    result=0
    def dfs(depth):

        if(depth==m):
            return 1

        return dfs(depth+1) * n



    print(f'#{test_case} {dfs(0)}')