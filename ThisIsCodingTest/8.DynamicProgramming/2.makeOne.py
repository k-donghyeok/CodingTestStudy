# 4:01

# 현재값을 5로 나눈다 3으로 나눈다 2로 나눈다 1뺀다
# dfs 로 4가지 연산을 진행
# 백트레킹으로 모든경우의 구하기
# 방문기록을 현재 값으로 무슨 연산을 했냐 2가지 값을 비교 해야할듯
# 현재값을 인덱스 연산안함을 0 1 2 3 4 를 5 3 2 1 순서대로
# 종료조건은 현재값이 1일때 min() 깊이
# 이걸 dp로 만드려면 탐색하는 경우의수 값을 저장해야한다
# dfs 는
n=int(input())

dx=[5,3,2]
dp=[0 for _ in range(n+1)]


def dfs(current):


    if(dp[current]!=0):
        return dp[current]
    if(current==1):
        return 0

    result = 99999999

    for i in range(4):
        if(i<3):
            if(current%dx[i]==0):
                nx=current//dx[i]
            else:
                continue

        elif(i==3):
            nx=current-1

        if(nx>=1):
            result=min(result,dfs(nx)+1)

    dp[current]=result
    return  result





print(dfs(n))



