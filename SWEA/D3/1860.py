# 1:42
# 2:33
# 음 사람들이 도착하는 시간을 인덱스로 배열에 표시 해서
# 해당 배열를 반복하면서 사람이 왔을때 붕어빵 갯수를 차감시키면됨
# 붕어빵은 인덱스가 지나가면서 계속 늘어남
# 그냥 구현 문제인거같음 완전탐색에
# 근데 사람들이 도착하는 시간을 11,111 이 최대인데 저크기만큼 만들필요가있을까?
# 입력으로 도착하는 시간들이 쭉 들어왔을떄 가장 큰 숫자만큼 배열을 만들면되지않을까?

T=int(input())

for test_Case in range(1,1+T):
    n,m,k = map(int,input().split())


    timeArr=[x for x in map(int,input().split())]
    maxIndex = sorted(timeArr)[-1]
    #print(timeArr)
    array=[0 for _ in range(maxIndex+1)]
    for i in timeArr:
        array[i]+=1

    #print(array)
    makeTime=0
    product=0
    result='Possible'
    for i in array:
        #print(f'{makeTime} {product}')
        if (makeTime == m):
            makeTime = 0
            product += k
        if (i != 0):
            if (product >= i):
                product -= i
                makeTime += 1
                continue
            else:
                result = 'Impossible'
                break



        makeTime += 1

    print(f'#{test_Case} {result}')


