# 3:47

# 말을 둘때 하 좌하 우하 이렇게 3가지 방향보고 없으면 둔다
# 완탐 으로 탐색 n번쨰 열까지 가서 말을 두면 결과값+1
# 2중 반복문으로 한번의경우 탐색은 했어 그다음 경우 탐색 하고싶은데
# 그걸 어떻게 하지
#
T=int(input())

for test_case in range(1,1+T):
    n=int(input())

    array=[ [0]*n for _ in range(n)]
   # print(array)
    dx=[-1,0,1] # 좌상 상 우상
    dy=[-1,-1,-1]
    result=0
    def dfs(y):
        global result

        if(y==n):
            result+=1
            return

        for x in range(n):
            stop=False
            for i in range(3):
                nx=x+dx[i]
                ny=y+dy[i]

                while(nx>=0 and nx<n and ny>=0 and ny<n):
                    if(array[ny][nx]==0):
                        nx=nx+dx[i]
                        ny=ny+dy[i]
                    else:
                        stop=True
                        break
                if(stop):
                    break
            if(stop):
                continue

            array[y][x]=1
            dfs(y+1)
            array[y][x]=0
    dfs(0)

    print(f'#{test_case} {result}')

