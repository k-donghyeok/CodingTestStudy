# 2차원 배열 반복문 안에 반복문 2개로 구역 나눠서 계산하기
# 상 하 2개로 나눠서 하면 될듯

T= int(input())

for test_case in range(1,1+T):
    n= int(input())
    array =[]
    for i in range(n):
        array.append(input().rstrip())


    #print(array)
    middle=n//2
    total=0
    for i in range(middle+1):
        for j in array[i][middle-i:middle+i+1]:
            #print(array[i][middle-i:middle+i+1])
            total+=int(j)
    for i in range(middle+1,n):
        for j in array[i][i-middle:middle-i]:
            #print(array[i][i-middle:middle-i])
            total += int(j)

    print(f'#{test_case} {total}')


