# 4:20

# 음 1차원 배열을 while 문으로 탐색하면 될거같은데
# 충전 횟수가 종료 조건으로 하고 충전할수있는곳이면 한번 충전으로 갈수있는 정류장 수만큼
# 충전횟수 + 정류장 이동할때 충전횟수 1감소
# 잠시만 이거 dp 냄새가 나는데 음 일단
# 선택한다 안한다 2개 가능 백트레킹인가

T=int(input())
for test_case in range(1,1+T):
    k,n,m = map(int,input().split())
    array=[0 for _ in range(n+1)] #1 일때 정류장
    for i in list(map(int,input().split())):
        array[i]=1
    print(array)
    result=9999
    def dfs(x,fuel,count):
        global result
        if(x==n):
            result=min(count,result)
            return

            return
        if(count>result):
            return



        if(array[x]==1):
            dfs(x + 1,k-1,count+1)
        if (fuel > 0):
            dfs(x+1,fuel-1,count)

    dfs(0,k,0)

    if(result==9999):
        result=0
    print(f'#{test_case} {result}')


