# 첫번째 행 아무곳이나 말을 놓으면 그 행에는 말을 놓을수없음
# 그열에도 말을 놓을수없음 그리고 대각선에도 말을 놓을수없음
# 내가 봐야하는 상태는 말을 놓을 좌표기준 열에 말이 있냐 행에말이있냐 대각선에 말이있냐
# 경우의수를 구하는 문제라 현재상태로 다시 돌아와야하네
# 필요한 값이 x,y 좌표 내가 방문한 좌표들 로 재귀함수 해야할듯
# 말을 n번 놓았을때가 종료조건 한 행에는 1개의 말만 놓을수있으므로
# 말을 둘수있으면 두고 행을 넘어가면서 행이 마지막에 도달하면 종료

T= int(input())


def check(x, y, visited):
    # 행검사
    for i in range(n):
        if (visited[y][i] == 1):
            return False
    # 열검사
    for i in range(n):
        if (visited[i][x] == 1):
            return False
    # 대각선 검사
    # 왼쪽 오른쪽 나눠서검사
    nx=x
    ny=y
    while(nx>=0 and ny>=0):
        if(visited[ny][nx] == 1):
            return False
        nx-=1
        ny-=1
    nx = x
    ny = y
    while(nx<n and ny>=0):
        if(visited[ny][nx] == 1):
            return False
        nx+=1
        ny-=1

    return True

for test_case in range(1,1+T):
    n=int(input())
    visited=[[0]*n for _ in range(n)]
    total=0
    def dfs(x, y, visited):
        global total
        while (x<n):
            if (y == n):
                total += 1
                return
            if(check(x, y, visited)):
                visited[y][x] = 1
                dfs(0, y + 1, visited)
                visited[y][x] = 0
            x += 1



    dfs(0,0,visited)

    print(f'#{test_case} {total}')




