#5 23
from collections import deque
T= int(input())




for test_case in range(1,T+1):
    n,l = map(int,input().split())
    array=[]
    for i in range(n):
        array.append(tuple(map(int,input().split())))
    result=0


    def search(index, total, score):
        global result
        if (total > l):
            return
        if (index == n):
            result = max(result, score)
            return

        search(index + 1, total + array[index][1], score + array[index][0])

        search(index + 1, total, score)

    search(0,0,0)

    print(f"#{test_case} {result}")
