from collections import  deque

T=int(input())

for test_case in range(1,1+T):
    n= int(input())

    array=[x for x in input().split()]
    #print(array)
    visited=[0 for _ in range(n)]
    #print(visited)
    temp=''
    resultArr=[]
    result=0
    def dfs1(depth):
        global  temp

        if(depth==n):
            #print(temp)
            #resultArr.append(temp)
            #여기에서 저울에 올리라는 소리인데

            #print(temp)
            resultArr.append(temp)


            return

        for i in range(n):
            if(visited[i]==0):
                visited[i]=1
                chu=''.join(array[i])
                temp1=temp
                temp=temp+' '+chu
                dfs1(depth+1)
                visited[i] = 0
                temp=temp1
    def dfs2(perm,index,left,right):
        global result

        # 모든 추 사용 완료
        if index == n:
            result += 1
            return

        current = perm[index]

        # 왼쪽
        dfs2(perm,index + 1, left + current, right)

        # 오른쪽
        if right + current <= left:
            dfs2(perm,index + 1, left, right + current)


    dfs1(0)
    for i in resultArr:
        perm = list(map(int, i.split()))
        dfs2(perm, 0, 0, 0)
    print(f'#{test_case} {result}')






    #print(f'#{test_case} {result}')


