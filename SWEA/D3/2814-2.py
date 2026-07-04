# 9:13

# 일단 그래프를 인접행렬 표현방식으로 변경해야함
# 배열의 인덱스가 노드번호이고 값으로 갈수있는 노드 번호들을 저장
# 모든 그래프를 표현한뒤 bfs로 큐에 값을 넣을때 길이를+1 하고 return 할때 최대길이 갱신

from collections import deque
T=int(input())

for test_case in range(1,1+T):
    n,m =map(int,input().split())

    graph=[[] for _ in range(n+1)]
    temp=[]
    for i in range(m):
        temp.append((input().split()))
    #print(temp)
    for i in temp:
        graph[int(i[0])].append(int(i[1]))
        graph[int(i[1])].append(int(i[0]))
    #print(graph)

    def dfs(current,length):
        global result
        result=max(result,length)

        for i in graph[current]:
            if(visited[i]==0):
                visited[i]=1
                dfs(i,length+1)
                visited[i]=0


    result = 0
    for start in range(1,n+1):
        visited = [0 for _ in range(n + 1)]
        visited[start]=1
        dfs(start,1)










    print(f'#{test_case} {result}')
#   4
# 1 -2 -3
#   5
#   6-  7