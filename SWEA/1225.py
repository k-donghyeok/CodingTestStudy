#01:34
from collections import deque

for _ in range(1,11):
    test=int(input())

    array=list(map(int,input().split()))
    que=deque()

    
    result=[]
    for i in array:
        que.append(i)
    
    index=1
    while(True):
        if(index==6):
            index=1
        
        target=que.popleft()
        if(target-index >0):
            que.append(target-index)
            index+=1
        else:
            que.append(0)
            break
    
    
    print(f"#{test}",end=' ')
    for i in que:
        print(f"{i}",end=' ')  
    print()
         

        
