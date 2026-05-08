# 기준을 1증가 시키면서 기준보다 오른쪽 있는거들중에서 최댓값 이랑 계산
# 시간초과뜸
# 최댓값 을 찾았으면 거기까지 반복문으로 합을 구하고 거기부터 다시


T = int(input())

for test_case in range(1,T+1):
    n = int(input())

    array=list(map(int,input().split()))

    total=0
    maxprice=array[len(array)-1]
    for i in range(len(array)-2,-1,-1):
        if(array[i]>maxprice):
            maxprice=array[i]
        else:
            total+=maxprice-array[i]

    print(f'#{test_case} {total}')















