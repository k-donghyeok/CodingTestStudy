# 14:24
# 14:42
# 지뢰찾기 를 구현을 하고  구현된 방식에서 탐색의 경우의수를 모두 해본뒤 제일 작은 횟수로 탐색
# 되는 경우를 찾아야하나
# 일단 지뢰찾기 구현은 dx dy 로 클릭한 좌표 기준 8방향 탐색을 진행하고 만약 진행한 칸의 값이 0이라면
# 다음 탐색 좌표로 que에 추가  que에 값이 없을때까지 탐색을 진행하고 다시 다음좌표 를 선택하게함
# 다음좌표를 선택하게 하는 방법으로는 dfs 로 해야할거같고 이미 탐색된곳은 탐색이 안되게
# visited 로 중복제거 근데 종료조건을 어떻게 잡지 좌측상단 부터시작해서 우측하단 좌표까지 완탐을해서
# 현재 좌표가 우측하단이면 종료 하도록
# visited 로 중복제거가 아니라 그냥 배열 원본을 수정을 시켜서 좌표값이
# 지뢰가 아닐때만 que에 추가하는걸로 하면 중복 탐색을 하지 않을거같은데
# 아니네 visitied 도 필요하네 dfs 로 탐색을 뒤로돌려서 다른경우를 탐색할때 필요하네
# 함수로 좌표가 주어지면 지뢰판안의 값이 변경하도록기능을 하나 만들어야할거같은데
# dfs 함수 안에서 좌표값을 변경하도록 하려닌까 복잡하네 좌표만 전달해주면 visited array
# 둘다 변경되도록 해보자
# 아 dfs 에서 다음 좌표값으로 뭘 넘겨줘야하지
# 그냥 계속 0,0 을 넘겨줘서 완탐을 한다?
from collections import  deque
N=int(input())

for test_Case in range(1,1+N):
    n=int(input())

    array=[]
    for i in range(n):
        array.append(input().rstrip())
    #print(array)
    visited=[[0]*n for _ in range(n)]
    #print(visited)
    for y in range(n):
        for x in range(n):
            if(array[y][x]=='*'):
                visited[y][x]=1


    dx=[0,0,-1,1,-1,-1,1,1] # 상하좌우 좌상하 우상우하
    dy=[-1,1,0,0,-1,1,-1,1]

    result=99999

    def update(current):
        count = 0
        que=deque()
        que.append(current)
        currentx,currenty=current
        while(que):
            x,y=que.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if (nx >= 0 and nx < n and ny >= 0 and ny < n):
                    if (visited[ny][nx] == 0):
                        if(array[ny][nx] == '*'):
                            count += 1
                        if(array[ny][nx]=='.'or array[ny][nx]==0):
                            que.append((nx,ny))

            array[currenty][currentx]=count

    def dfs(current, depth, visited):
        x,y=current
        global result

        for y in range(n):
            for x in range(n):
                if (visited[y][x] == 0):
                    visited[y][x] = 1
                    update(current)
                    dfs()











