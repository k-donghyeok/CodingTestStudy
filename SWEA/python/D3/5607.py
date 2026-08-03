# 9:33


# 윗부분이 r번  반복해서 n부터 1식감소 하면서 곱
# 아래 부분이  r번 반복해서 r 부터 1식감소 하면서 곱

T=int(input())

for test_Case in range(1,1+T):
    n,r = map(int,input().split())

    dp = [[0] * (r + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, min(i, r) + 1):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 1234567891

    print(f'#{test_Case} {dp[n][r]}')