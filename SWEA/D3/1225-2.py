# 5:31

from collections import deque

for _ in range(1,11):
    test_Case =int(input())

    que=deque()
    temp=[x for x in input().split()]
    for i in temp:
        que.append(i)
    index=0
    while(True):
        if(index>=5):
            index=0
        index+=1
        current=int(que.popleft())
        current-=index
        if(current>0):
            que.append(str(current))
        else:
            que.append('0')
            break
    result=''

    result=result+''.join(que)
    print(f'#{test_Case}',end=' ')
    for i in range(len(result)):
        print(f'{result[i]}',end=' ')
    print()

