# 8:35

# 깊이와 연료수,충전수 를 인자로 들고 깊이가 n 일때 충전수 갱신


T=int(input())

for test_Case in range(1,1+T):
    k,n,m = map(int,input().split())

    array=[0 for _ in range(n+1)]

    temp=[int(x) for x in input().split()]

    for i in temp:
        array[i]+=1
    result=99999
    visited=[]
    def dfs(depth,fuel,count):

        global result
        if((depth,fuel,count) in visited):
            return
        else:
            visited.append((depth,fuel,count))
            #print(visited)
        if(depth==n):
            result=min(result,count)
            return

        if(fuel<=0):
            if(array[depth]==1):
                dfs(depth+1,k-1,count+1)
            else:
                return
        else:
            if(array[depth]==1):
                dfs(depth + 1, k - 1, count + 1)
                dfs(depth + 1, fuel-1, count)
            else:
                dfs(depth + 1, fuel - 1, count)



    dfs(0,k,0)
    if(result==99999):
        result=0
    print(f'#{test_Case} {result}')