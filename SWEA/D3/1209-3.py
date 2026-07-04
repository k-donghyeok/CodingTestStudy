#1:40
#1:50
#점부 완탐으로 다 더해서 다더했을때 최댓값 갱신


for _ in range(1,11):

    test_case=int(input())
    array=[]
    for y in range(100):
        array.append(input().split())

    #print(array)
    result=0
    #행
    for y in range(100):
        total = 0
        for x in range(100):
            total+=int(array[y][x])
        result=max(result,total)
    #열
    for x in range(100):
        total=0
        for y in range(100):
            total+=int(array[y][x])
        result=max(result,total)
    #대각선
    total = 0
    for x in range(100):

        for y in range(x,x+1):
            total += int(array[y][x])
        result = max(result, total)
    # 대각선
    total = 0
    for x in range(99,-1,-1):

        for y in range(x,x+1):
            total += int(array[y][x])
        result = max(result, total)
    print(f'#{test_case} {result}')