# 격자퐌 확인
# 2차원 배열로 맵이 주어지는데 입력받은 조건에 따라 배열의 값을 변경해야함
# 전차이동시 dx dy 써서 이동하고 포탄이동시에도 dx dy 써서 이동하자
# 딕셔너리로 전차의 움직임이 있을때 좌표, 방향을 수정

T= int(input())
for test_case in range(1,1+T):

    h,w = map(int,input().split())

    array=[]
    for i in range(h):
        array.append(list(input().rstrip()))
    #print(array)
    n=int(input())
    move=input().rstrip()
    #print(n)
    #print(move)

    def find():
        global  x
        global  y
        global direction
        stop = False
        for i in range(h):
            for j in range(w):

                if(array[i][j]=='^'):
                    x=j
                    y=i
                    direction=0

                    stop=True
                    break
                elif(array[i][j] == 'v'):
                    x = j
                    y = i
                    direction = 1

                    stop = True
                    break
                elif (array[i][j] == '<'):
                    x = j
                    y = i
                    direction = 2

                    stop = True
                    break
                elif (array[i][j] == '>'):
                    x = j
                    y = i
                    direction = 3

                    stop = True
                    break
            if (stop):
                break


    moveTank={'U':[(0,-1),0],
            'D':[(0,1),1],
            'L':[(-1,0),2],
            'R':[(1,0),3],} # 상 하 좌 우

    moveBullet=[[0,-1],
                [0,1],
                [-1,0],
                [1,0]] #상 하 좌 우
    x=0
    y=0
    direction=0
    find()
    #print(f'{y},{x} {direction}')
    CurentTank=['^','v','<','>']
    for i in move:
        #print(i)
        if(i in list(moveTank.keys())):
            dx=x+moveTank.get(i)[0][0]
            dy=y+moveTank.get(i)[0][1]
            direction=moveTank.get(i)[1]
            array[y][x]=CurentTank[direction]
            if(dx>=0 and dx<w and dy>=0 and dy<h):
                if(array[dy][dx]=='.'):
                    array[y][x]='.'
                    x=dx
                    y=dy
                    array[y][x] = CurentTank[direction]




        elif(i =='S'):
            dx=x
            dy=y
            while(0<=dx<w and 0<=dy<h):
                if (array[dy][dx] == '*'):
                    array[dy][dx] = '.'
                    break
                if(array[dy][dx] == '#'):
                    break
                dx+=moveBullet[direction][0]
                dy+=moveBullet[direction][1]

    print(f'#{test_case}',end=' ')
    for i in range(h):
        for j in range(w):
            print(array[i][j],end='')
        print()









