# 4:36
# 4:53
for _ in range(1,11):
    test_case = int(input())
    array=[]
    for i in range(100):
        array.append(list(map(int,input().split())))

   # print(array)
    result=0
    #행
    sum = 0
    for i in range(100):
        for j in range(100):
            sum+=array[i][j]
        result = max(sum, result)
        sum = 0


    #열
    sum=0
    for i in range(100):
        for j in range(100):
            sum+=array[j][i]
        result = max(sum, result)
        sum = 0


    #대각선
    sum=0
    for i in range(100):
        sum+=array[i][i]

    result = max(sum, result)

    sum = 0
    for i in range(100):
        sum+=array[i][-i-1]
    result = max(sum, result)

    print(f'#{test_case} {result}')
