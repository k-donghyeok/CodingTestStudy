# 2:55

# 경우의 수 중에서 최고값찾기
# dfs 칼로리 만 들고가면될듯
# 종료 조건 마지막 재료 까지 왔을때


T=int(input())

for test_Case in range(1,1+T):
    n,l = map(int,input().split())

    hamber=[]
    for i in range(n):
        score,cal=map(int,input().split())
        hamber.append((score,cal))

    #print(hamber)
    result=0
    def dfs(start,current,score,depth):
        global result
        if(current>l):
            return
        if(depth>len(hamber)):
            return
        result=max(result,score)

        for i in range(start,len(hamber)):
            nx=current+hamber[i][1]
            if(nx<=l):
                dfs(i+1,nx,score+hamber[i][0],depth+1)

        #dfs(start,current,score,depth+1)
    dfs(0,0,0,0)
    print(f'#{test_Case} {result}')
