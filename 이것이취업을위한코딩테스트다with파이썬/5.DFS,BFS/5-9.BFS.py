from collections import deque


# 1.탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입 하고 방문처리를 한다.
# 3. 2번의 과정을 더 이상 수행할수 없을 때까지 반복한다 

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
result=[]
visited=[0]*9
que = deque()
def search(v,_graph,visited):
    que.append(v)
    visited[v]=1
    

    while(que):
        v=que.popleft()
        result.append(v)
        for i in _graph[v]:
            if(visited[i]==0):
                que.append(i)
                visited[i]=1
                
                
        
                
search(1,graph,visited)
print(result)

    
