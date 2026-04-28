T=int(input())
for test in range(1,T):
    n =int(input())

    array = [[i*n + j for j in range(1,n+1)] for i in range(n)]
    visited = [[0]*n for _ in range(n)]

    dx=[1,0,-1,0]  # 우 하 좌 상
    dy=[0,1,0,-1]
    count=0
    x=0
    y=0
    visited[0][0]=1
    while(count < pow(n,2)-1):
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            while(nx >=0 and nx<n and ny>=0 and ny<n):
                if(visited[ny][nx]==0):
                    count+=1
                    x=nx
                    y=ny
                    visited[y][x]=array[(count)//n][(count)%n]
                    nx=x+dx[i]
                    ny=y+dy[i]
                else:
                    break
                
    print(f"#{test}")
    for i in range(n):
        for j in range(n):
            print(f"{visited[i][j]}",end=' ')
        print()





