n,m= map(int,input().split())
graph=[]
count=0
for _ in range(n):
    graph.append(list(map(int,input())))

visited = [[0] * m for _ in range(n)]


dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

def search(x,y,graph,visited):
    visited[x][y]=1
   
    for i in range(4):
        
        nx=x+dx[i]
        ny=y+dy[i]
        if((nx>=0 and nx<n) and (ny>=0 and ny<m)):
            if(graph[nx][ny]==0 and visited[nx][ny]==0):
                
                search(nx,ny,graph,visited)
            
        


for row in range(n):
    for col in range(m):
        if(visited[row][col]==0 and graph[row][col]==0):
            search(row,col,graph,visited)
            count+=1

print(count)
        

            