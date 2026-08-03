#11:10

# 2차원 배열에 x,y 좌표에 놓을때 상 하 좌우 탐색후
# 반대대는 돌을 찾아서 존재하면 내돌로 바꾸면됨
# 돌을 찾을때는 보드의 끝에서 부터 찾는걸로
# 그냥 보드의 끝에서 부터 같은 돌을 찾아서 찾으면 거기부터 내 좌표까지
# 해당하는 열or행 을 내돌로 변경
# 입력받은 배열을 다돌면 종료 후 출력

T=int(input())

for test_Case in range(1,1+T):
    n,m = map(int,input().split())

    bord=[[0]*n for _ in range(n)]

    moves=[]


    dx=[0,0,-1,1,-1,-1,1,1] # 상 하 좌 우 좌상 좌하 우상 우하
    dy=[-1,1,0,0,-1,1,-1,1]

    for i in range((n//2)-1,(n//2)+1):
        for j in range(i,i+1):
            bord[i][j]=2
            bord[i][-j-1]=1

    def change(x, y, color):

        result=[]
        start = (x, y)
        for i in range(8):

            stop = True
            temp = []
            x=start[0]
            y=start[1]
            while(stop):
                nx = x + dx[i]
                ny = y + dy[i]
                if(nx>=0 and nx<n and ny>=0 and ny<n):
                    if(bord[ny][nx]!=0):
                        if(bord[ny][nx]!=color):
                            temp.append((nx,ny))
                            #print(temp,i)
                            x=nx
                            y=ny
                        else:
                            result.append(temp)
                            stop=False
                    else:
                        stop=False
                else:
                    stop=False
        for i in result:
            for j in i:
                bord[j[1]][j[0]]=color

    for i in range(m):
        moves.append(list(map(int,input().split())))
    #print(moves)
    for move in moves:
        bord[move[1]-1][move[0]-1]=move[2]
       # print(bord)
        change(move[0]-1,move[1]-1,move[2])
        #print(bord)



    black=0
    white=0
    #print(bord)
    for i in bord:
        for j in i:
            if(j==1):
                black+=1
            elif(j==2):
                white+=1
    print(f'#{test_Case} {black} {white}')

