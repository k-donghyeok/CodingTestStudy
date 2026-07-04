#1:53
# 2:09
#배열 삽입 삭제
#큐에 숫자들을 넣고 while 문으로 큐에서꺼낸 숫자에서 감소를 시켰을때 0보다 작으면 탈출
from collections import deque

for _ in range(1,11):
    test_case=int(input())

    que=deque()
    temp=[x for x in input().split()]
    #print(temp)
    for i in temp:
        que.append(int(i))

    i=1
    while(True):
        current=que.popleft()
        current-=i
        if(current<=0):
            que.append(0)
            break
        que.append(current)
        i+=1
        if(i>5):
            i=1
    print(f'#{test_case}',end=' ')
    for i in que:
        print(i,end=' ')
    print()