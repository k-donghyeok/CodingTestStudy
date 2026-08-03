# 7:02

# 열 탐색하면서  시작이 빨강 마지막이 파랑이면 결과에 +1인데
# 시작이빨강 마지막이파랑인지 어떻게 검사할수있을까
# 빨강이면 그냥 아래로 쭉 밀어서 파랑 나올떄까지 검사할까
# 그래서 파랑 나오면 다시 빨강 나올때까지 쭉밀고 빨강 나오면 다시 파랑

# 1빨 2파
for test_Case in range(1,11):
    n=int(input())

    array=[]
    for y in range(n):
        array.append(input().split())
    dx=[0]
    dy=[1]
    result=0
    for x in range(n):
        state=-1
        for y in range(n):
            if(array[y][x]=='1'):
                state=1
            elif(array[y][x]=='2'):
                if(state==1):
                    result+=1
                    state=-1
    print(f'#{test_Case} {result}')









