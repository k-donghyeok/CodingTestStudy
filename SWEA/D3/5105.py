# 3:28

# bfs 같은데 간곳이 3 이면 종료
# 갔던곳을 체크해야하나? 체크하고 만약에 갈수있는곳이 갔던곳밖에 없으면
# 돌아가는걸로? 큐에 현재 위치에서 갈수있는 곳들을 넣고
# 하나씩 꺼내면서 방문체크
# 상태를 되돌릴필요는 없을듯 bfs 라서 동시에 다른곳들이 진행되닌까
# 재귀로 구현을해야하나 반복문으로 구현을 해야하나 흠
# 반복문이 좀 더 편할거같은데 4방향 모두 보내기에
# 음 재귀 써야겠는데 아닌가 카운트가 1씩늘어날때
# 카운트를 어떻게 1씩증가 시키지
from collections import  deque
T=int(input())

for test_case in range(1,1+T):
    n=int(input())

    array=[]
    for i in range(n):
        array.append(input().rstrip())

    visited = [[0] * n for _ in range(n)]

    dx=[0,0,-1,1] # 상 하 좌 우
    dy=[-1,1,0,0]
    x=0
    y=0

    for i in range(n):
        for j in range(n):
            if(array[i][j]=='2'):
                x=j
                y=i



    que=deque()
    que.append((x,y))
    result=0
    while(que):
        x,y= que.popleft()


        if(array[y][x]=='3'):
            result=1
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(nx>=0 and nx<n and ny>=0 and ny<n):
                if((array[ny][nx]=='0' or array[ny][nx]=='3') and visited[ny][nx]==0):
                    que.append((nx, ny))
                    visited[ny][nx]=visited[y][x]+1
    if(result):
        print(f'#{test_case} {visited[y][x]-1}')
    else:
        print(f'#{test_case} {result}')

