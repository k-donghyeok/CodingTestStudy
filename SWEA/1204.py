T = int(input())

for test in range(1,T+1):
    count=int(input())

    visited=[0 for _ in range(101)]
    scores=list(map(int,input().split()))

    for i in scores:
        visited[i]+=1

    maxCount=max(visited)
    maxNum=0
    for i in range(len(visited)):
        if(visited[i]==maxCount):
            maxNum=i
    
    print(f"#{test} {maxNum}")