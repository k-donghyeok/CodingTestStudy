#그래프 를 인접 행열 방식으로 표현
#그래프는           0
#             (7)/  \(5)
#               1    2

INF=999999999
graph=[
    [0,7,2],
    [7,0,INF],
    [5,INF,0]
]

print(graph)


#그래프 를 인접 리스트 방식으로 표현
#그래프는           0
#             (7)/  \(5)
#               1    2
graph.clear

graph=[[] for _ in range(3) ]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))
