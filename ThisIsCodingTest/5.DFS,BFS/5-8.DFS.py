

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
isSearch=[0]*9

def search(isSearch,i,_graph):
    isSearch[i]=1
    result.append(i)

    for i in _graph[i]:
        if(isSearch[i]==0):
            search(isSearch,i,_graph)
        

search(isSearch,1,graph)
print(result)