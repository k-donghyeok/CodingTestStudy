# 12:00 ~12:12
# 12:22 ~ 1 :05
# 2=s , 1=n  0은 위로 1이 없으면 사라짐 1은 아래로 0이 없으면 사라짐
# 그럼 위에 1 아래에 2 사이에 있으면 그 사이 범위는 판위에 남아있네
# 같은 열에 그럼 위쪽에 1 아래에 2 사이인 구간이 있는지 검사하면됨
# 완탐으로 열 검사를 하면 되겠다

for test_case in range(1,11):
    n= int(input())
    array=[]
    for i in range(n):
        array.append(input().split())

    total=0

    for i in range(n):
        topN = n
        downS = 0
        for j in range(0,n):
            if(array[j][i]=='1'):
                topN=j
                break
        for k in range(n-1,-1,-1):
            if(array[k][i]=='2'):
                downS=k
                break
       # print(f'{topN} {downS}')
        if(topN<downS):
            startN = False
            finishS = False
            for _ in range(topN,downS+1):
                if(array[_][i]=='1' and not startN):
                    startN=True
                    continue
                if(array[_][i]=='2' and startN):
                    if(_ == downS):
                        total += 1
                    else:
                        finishS=True
                        continue
                if(array[_][i]=='1' and startN and finishS):
                    total+=1
                    startN=True
                    finishS=False
            #print(f'{total}')

    print(f'#{test_case} {total}')
