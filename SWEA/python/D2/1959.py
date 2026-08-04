# 배열 2개를 만들어서 근데 위치 변경이 가능하다는데 위치변경에 대한 변수가
# 완전탐색인거 같고 큰 배열의 길이 - 작은 배열의 길이 +1 만큼 반복해서 그중에서
# 최댓값 구하면될듯
# a는 0부터 끝까지 가고 b는 0더하기 i 부터 a 길이만큼
T=int(input())

for test_case in range(1,1+T):
    n,m = map(int,input().split())

    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    count=0
    sum=0
    if(n<m):
        result = 0
        count = m - n + 1
        for i in range(count):
            for j in range(n):
                sum += a[j] * b[j + i]
            result = max(sum, result)
            sum = 0
    elif(n>=m):
        result = 0
        count = n - m + 1
        for i in range(count):
            for j in range(m):
                sum += b[j] * a[j + i]
            result = max(sum, result)
            sum = 0
   


    print(f'#{test_case} {result}')