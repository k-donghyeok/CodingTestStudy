# 10:20

# dx dy 로 이동 관리 하고 bfs로 큐에 현재상태에서 갈수있는곳을 담은다음
# 반복문으로 4방향 검사를해 갈수있는 곳이면 큐에 추가한다
# visited 로 갔던곳이면 못가게한다 아이게 좀 애매하네

from collections import deque

for _ in range(1,11):
    test_case=int(input())

    array=[]
    for y in range(16):
        array.append(input().rstrip())
    start=0
    goal=0
    for y in range(16):
        for x in range(16):
            if(array[y][x]=='2'):
                start=(x,y)
            if (array[y][x] == '3'):
                goal = (x, y)
    #print(start,goal)
    dx=[0,0,-1,1] # 상 하 좌 우
    dy=[-1,1,0,0]

    que=deque()
    visited=[[0]*16 for _ in range(16)]
    que.append(start)
    result=False
    while(que):

        current=que.popleft()
        #print(current)
        x=current[0]
        y=current[1]
        if(goal==current):
            result=True
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(nx>=0 and nx<16 and ny>=0 and ny<16):
                if(array[ny][nx]=='0' or array[ny][nx]=='3'):
                    if(visited[ny][nx]==0):
                        visited[ny][nx]=1
                        que.append((nx,ny))



    if(result):
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
