# 6:00
# 6:36

# 2차원 배열의 탐색 범위를 조절하는문제
# 중앙에서 얼만큼 떨어져있는지 기준으로 얼만큼떨어져있는지
# 위 아래 2개로 나눠서 처리하는게 편할거같음

T=int(input())

for test_Case in range(1,1+T):
    n=int(input())
    array=[]
    for i in range(n):
        array.append(input().rstrip())

    middle= n//2
    result=0

    for i in range(n):
        if(i<middle):
            for _ in array[i][middle-i:middle+i+1]:
                result+=int(_)
        else:
            for j in range(n-i-1,n-i):
                for _ in array[i][middle-j:middle+j+1]:
                    result += int(_)

    print(f'#{test_Case} {result}')