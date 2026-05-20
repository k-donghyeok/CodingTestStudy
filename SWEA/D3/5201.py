# 10:41
# 11:06
# 화물 용량이 최대로 되도록 옮기려면
# 큰 트럭이 가능한 제일 큰 화물을 들고가야함
# 화물을 내림차순으로 정렬하고 트럭도 내림차순으로 정렬후
# 화물을 열로 트럭을 행으로 반복문을 돌려서
# 해당화물을 트럭이 운반가능한지 보고 가능하면
# 다음 트럭과 화물로 불가능하면 다음화물로 트럭은 동일하게



T=int(input())

for test_case in range(1,1+T):
    n,m=map(int,input().split())

    containers=[int(x) for x in input().split()]
    trucks=[int(x)for x in input().split()]

    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    total=0

    start=0
    container = 0
    while(start<len(trucks)):
        if(container>=len(containers)):
            break
        for truck in range(start,len(trucks)):
            if(trucks[truck]>=containers[container]):
                #print(f'넣음{trucks[truck]} {containers[container]}')
                total+=containers[container]
                container+=1
                start+=1
                break
            else:
                #print(f'탈출{trucks[truck]} {containers[container]}')
                container+=1
                break



    print(f'#{test_case} {total}')
    # for i in range(len(truck)):
    #     for j in range(len(container)):

