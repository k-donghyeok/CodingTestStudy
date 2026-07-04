#11:56

# 경우의 수 구하기 dfs 선택 범위를 지정해서 중복을 제거
# 선택의 범위를 현재 값부터 12까지
# 선택한다 안한다 2개로 나뉨 선택하면 current+1 dksgkaus current 을 dfs()
# 인자로 현재까지의 합도 들고가자 그래서 탈출조건으로 합이 원하는 값일때 그거보다 클때
# 중복제거는 범위로 하기때문에 visited 필요없어 보임

T=int(input())

for test_Case in range(1,1+T):
    n,k =map(int,input().split())

    array=[int(x) for x in range(1,13)]

    #print(array)
    result=0
    def dfs(current,total,depth):
        global result
        if(total>k):
            return
        if(total==k and depth==n):
            result+=1
            return
        if(current>12):
            return
        if(depth>n):
            return

        for i in range(current,13):
            dfs(i+1,total+i,depth+1)

    dfs(1,0,0)

    print(f'#{test_Case} {result}')
