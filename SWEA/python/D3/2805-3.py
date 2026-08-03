# 10:43
# 11:05

# 배열 탐색 문제
# 구간을 나눠서 하는게 좋음
# 중앙에서 떨어진 거리 a 이면 middle-a:middle+a
# 배열의 열을 전부 반복문 돌리면서 0이면 중앙과 2 떨어져있고 middle-2:middle+2
# 까지 슬라이싱
# 아 또 ㅁ가히네 중앙에서 떨어진 거리 중앙까지는 문제 없는데 중앙을 넘어가면
# 그냥 상 하 나누자
T=int(input())

for test_case in range(1,1+T):
    n=int(input())
    array=[]
    for _ in range(n):
        array.append(input().rstrip())

    #print(array)

    middle=n//2
    result=0
    # for y in range(middle):
    #     temp=array[y][middle-y:middle+y+1]
    #
    #     for x in temp:
    #         result+=int(x)

    for y in range(n):
        temp = array[y][abs(middle - y):n-abs(middle-y)]

        for x in temp:
            result+=int(x)
    print(f'#{test_case} {result}')