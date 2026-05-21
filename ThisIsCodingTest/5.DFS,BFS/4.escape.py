from collections import deque

n,m = map(int,input().split())

graph=[]
visited = [[0] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input())))

dx=[0,-1,0,1] #서 북 남 동
dy=[-1,0,1,0]


que=deque()





def search():
    
    que.append([0,0])
    distance[0][0]=1
    visited[0][0]=1
    while(que):
        
        x,y=que.popleft()
        
        if(x==n-1 and y==m-1):
            print(distance[x][y])
            break
        
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if((nx>=0 and nx<n )and (ny>=0 and ny<m) and graph[nx][ny]==1 and visited[nx][ny]==0):
                que.append([nx,ny])
                visited[nx][ny]=1
                distance[nx][ny]=distance[x][y]+1
                
                
                
                
                
search()

