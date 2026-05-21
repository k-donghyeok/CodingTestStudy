#5:35

# 타일 3가지 반복해서 선택 가로 길이가 n이면 종료
# 현재 길이를 넘겨주자 선택한 타일에 맞게 더해서 재귀호출
# 이거 길이가 2인 타일이 2개있는데 이거 중복검사를 해야하나?
# 안해도될듯

n=int(input())
dx=[2,1,2]

dp=[-1 for _ in range(n+1)]
def dfs(current):

    if(dp[current]!=-1):
        return dp[current]

    if(current<=1):
        return 1

    result = 0
    for i in range(3):


        nx=current-dx[i]
        if(nx>=0):
            result+=dfs(nx)


    dp[current] = result
    return result






print(dfs(n))