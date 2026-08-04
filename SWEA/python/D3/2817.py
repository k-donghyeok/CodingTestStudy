# 5:48
# 6:30
T=int(input())

for test_case in range(1,1+T):
    n,k = map(int,input().split())

    array=[int(x) for x in input().split()]
    temp=[]
    result=0
    visited=['0' for _ in range(n)]

    #print(visited)
    def dfs(index,total,graph):
        global result
        if (total == k):

            result += 1
            return

        if(index==len(array)):
            return

        if(total>k):
            return


        for i in range(index,len(array)):
            if(graph[i]=='0'):
                graph[i]='1'
                dfs(i+1,total+array[i],graph)
                graph[i] = '0'


    dfs(0,0,visited)

    print(f'#{test_case} {result}')
