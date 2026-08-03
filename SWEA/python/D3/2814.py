# 2:57

# 음 n개의 정점과 m 개의 간선으로 구성된 가중치가 없는 무방향 그래프
# 가중치가 없다는게 무슨말인지 무방향이 무슨말인지 모르겠네
# 1 - 2 - 3 이면 길이가 3
# 1 이면 길이가 1  인건가
# 그러면 같은 행에 있거나 같은 열에 있으면 길이를 더해줘야겠네
# 그럼 2차원 배열에 일단 그래프를 그리고
# 2차원 배열에서 근데 입력으로
# 1 2
# 3 2 가 1 - 2 - 3 이라면
# 왜 2번 노드 정보는 안주는거지 순서가없네
# 그럼 입력 받은 정보로 모르겠네
# 1 - 2 - 3
#    ㅣ
#     4
#일때는 입력으로
# 4 3
# 1 2
# 2 4
# 3 2
# 이렇게 들어오는건가 이렇게 들어오면
# 그래프를 어떻게 그리지 저 입력으로
from collections import deque
T=int(input())

for test_case in range(1,1+T):
    n,m= map(int,input().split())

    graph=[[]for _ in range(n+1)]

    for i in range(m):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited=[0 for _ in range(n+1)]
    result=0
   # print(visited)
    #print(graph)
    def dfs(node,depth):
        global  result
        result = max(result, depth)
        if(len(graph[node])>=1):
            for j in graph[node]:
                if(visited[j]==0):
                    visited[j]=1
                    dfs(j,depth+1)
                    visited[j] = 0


    for i in range(1,1+n):
        visited[i]=1
        dfs(i,1)
        visited[i]=0
    print(f'#{test_case} {result}')
    #    4
    #    ㅣ
    # 2- 1- 3
    #    ㅣ
    #    5 - 6

    # 탐색의 시작점을 모든 노드가 해보도록 하고 그중에서 깊이가 가장 깊은거로 하면되네
    #
