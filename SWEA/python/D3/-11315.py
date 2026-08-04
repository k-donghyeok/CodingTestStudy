#1:31
#2:03
# 2차원 배열 공간 에서 연속된 값확인 좌표가 선택되면 이동이 반복됨
# 방향이 있고 2차원 배열의 이동 dx dy 로 관리하자
# 반복문으로 한방향으로 이동하다가 길이가 5이면 탈출
# 시작점 찾기는 2차원 배열의 완탐 한방향으로 이동했던 길을 visited 에넣고
# 시작점 찾기에 제외해도되나? 안될듯
# 아 어차피 길이가 5이면 탈출하기 때문에 중복검사 이루어 지지않음
# 그냥 시작점보다 왼쪽에 있는 값(지나온)들은 고려하지 않아도 됨
# 방향이 왼쪽 은 볼필요가없음 시작점 찾기가 완탐이라
# 오른쪽 아래  우하 좌하 이렇게 4개만 보면될듯
# dfs 사용해서 연속된 길이 측정하면될듯
# 잠시만 한방향 탐색이 아니라 갈수있는 모든곳을 보는데 dfs는
#
T=int(input())

for test_Case in range(1,1+T):
    n=int(input())
    board=[]
    for i in range(n):
        board.append(input().rstrip())

    dx=[1,0,1,-1] #우 하 우하 좌하
    dy=[0,1,1,1]
    result='NO'
    stop=False
    def dfs(x,y):
        global  result
        global  stop
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            length=1
            while(nx>=0 and nx<n and ny>=0 and ny<n):
                if(board[ny][nx]=='o'):
                    nx=nx+dx[i]
                    ny=ny+dy[i]
                    length+=1
                    if (length >= 5):
                        result = 'YES'
                        stop = True
                        break
                else:
                    break
            if(stop):
                break




    for y in range(n):
        for x in range(n):
            if(board[y][x]=='o'):
                dfs(x,y)


    print(f'#{test_Case} {result}')