#10:50

# 최소거리 구하기 그리디 아니면 bfs 인데
# 미로 bfs 확률 높음 2차원 배열 형태 임으로 ds dy 로 움직임 관리
# 큐에 현재좌표에서 갈수있는 곳들을 추가
# visted[next] 에 현재까지 거리 + 1 갱신 해주면서 이동
# 도착지로 못가는 경우도 있으려나?
# 일단 도착하면 그때의 visited 값이 최소 거리

from collections import deque
T=int(input())

for test_Case in range(1,1+T):
    n=int(input())

    array=[]
    for y in range(n):
        array.append(input().rstrip())
    #print(array)
    visited=[[-1]*n for _ in range(n)]
    #print(visited)
    que=deque()
    start=0
    goal=0
    for y in range(n):
        for x in range(n):
            if(array[y][x]=='2'):
                start=(x,y)
            if(array[y][x]=='3'):
                goal=(x,y)
    #print(start,goal)
    que.append(start)
    dx=[0,0,-1,1] # 상 하 좌 우
    dy=[-1,1,0,0]
    visited[start[1]][start[0]]=0
    result=0
    while(que):

        current=que.popleft()
        x=current[0]
        y=current[1]
        #print(current,goal)
        if(current==goal):
            result=visited[y][x]-1
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(nx>=0 and nx<n and ny>=0 and ny<n):
                if(array[ny][nx]=='0' or array[ny][nx]=='3'):
                    if(visited[ny][nx]==-1):
                        visited[ny][nx]=visited[y][x]+1
                        que.append((nx,ny))
    if(result<0):
        result=0

    print(f'#{test_Case} {result}')