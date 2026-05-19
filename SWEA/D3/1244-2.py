# 1:09
from collections import deque
# 상태를 다시 돌릴 필요없을듯 되돌아갈필요가없음
# 음 자리 바꿔주는거 완탐말고 다르게 구현해야겠는데 속도가 너무 느리네

T=int(input())

for test_Case in range(1,1+T):
    array,n=input().split()

    n=int(n)
    array=[x for x in array]
    visited=set()
    result=0
    def dfs(array,depth):
        global  result
        if (depth == n):
            temp = ''.join(array)
            # print(temp)
            intArr = int(temp)
            result = max(result, intArr)
            return

        if((''.join(array),depth) in visited):
            #print(array,visited)
            return
        else:
            visited.add((''.join(array),depth))



        for i in range(len(array)):
            for j in range(i+1,len(array)):
                #print(array)
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
                #print(array)
                dfs(array,depth+1)
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                #print(array)
    dfs(array,0)

    print(f'#{test_Case} {result}')

