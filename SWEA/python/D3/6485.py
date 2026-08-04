# 12:42

# 노선은 정류장 번호 a에서 b 사이의 정류장만 다닌다
# 범위가 주어지고 정류장 들이 주어진다
# 정류장들은 배열로 나타낼수있을거같다 인덱스로
# 범위를 입력받고 해당 범위의 인덱스 를+
# 카운팅 방식같은데
# 범위를 배열에 append 하고 하나씩 꺼내서
# (1,3) for i in range(arr[0],arr[1]+1):
#           result[i]+=1

T=int(input())

for test_case in range(1,1+T):
    n=int(input())

    array=[]
    for _ in range(n):
        array.append(tuple(map(int,input().split())))

    p=int(input())
    busStop = []
    for i in range(p):
        busStop.append(int(input().rstrip()))
    busMax=max(busStop)
    arrayMax=max(array, key=lambda x: x[1])[1]
    if(busMax>arrayMax):
        temp=[0 for _ in range(max(busStop)+1)]
    else:
        temp = [0 for _ in range(max(array, key=lambda x: x[1])[1] + 1)]
    #print(max(array, key=lambda x: x)[1]+1)
    for i in array:
        for j in range(i[0],i[1]+1):
            temp[j]+=1
    #print(array)
    #print(busStop)
    #print(temp)

    print(f'#{test_case}',end=' ')
    for i in busStop:
        print(temp[i],end=' ')
    print()