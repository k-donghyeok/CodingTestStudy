# 11:09
# 12:04
# 방향 2개 배열 완탐으로 시작점 찾고
# 방향 2개 쭉 탐색 가능할떄까지 갔을때 길이가 3이면 결과값+

# dx dy 로 탐색하자

T=int(input())

for test_case in range(1,1+T):
    n,m =map(int,input().split())

    array=[]
    for y in range(n):
        array.append(input().split())

    # 1흰 0검

    dx=[1,0,0,-1] #  우 하 상 좌
    dy=[0,1,-1,1]
    result=0

    for y in range(n):
        for x in range(n):
            if(array[y][x]=='1'):
                for j in range(2,4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if (nx >= 0 and nx < n and ny >= 0 and ny < n):
                        if(array[ny][nx]=='0'):
                            for i in range(2):
                                length = 1
                                nx=x+dx[i]
                                ny=y+dy[i]
                                if(nx>=0 and nx<n and ny>=0 and ny<n):

                                    while(nx>=0 and nx<n and ny>=0 and ny<n):
                                        if(array[ny][nx] == '0'):
                                            break
                                        elif(array[ny][nx] == '1'):
                                            length+=1
                                            nx=nx+dx[i]
                                            ny=ny+dy[i]
                                    if (length == m):
                                       # print(x,y)
                                        result += 1

                    else:
                        for i in range(2):
                            length = 1
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if (nx >= 0 and nx < n and ny >= 0 and ny < n):

                                while (nx >= 0 and nx < n and ny >= 0 and ny < n):
                                    if (array[ny][nx] == '0'):
                                        break
                                    elif (array[ny][nx] == '1'):
                                        length += 1
                                        nx = nx + dx[i]
                                        ny = ny + dy[i]
                                if (length == m):
                                    # print(x,y)
                                    result += 1

# 조건을 만족할때 더이상 갈수없을때 길이가 m 일때
# 갈수있는데 길이가 3이면 break 할까






    print(f'#{test_case} {result}')