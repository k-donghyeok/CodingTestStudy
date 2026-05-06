T=int(input())

for test in range(1,T+1):
    testcase=input()

    array=[]

    array=list(map(int,input().split()))

    visited=[0 for i in range(101)]

    for i in array:
        visited[i]+=1

    maxcount=max(visited)
    result=0
    for i in range(len(visited)):
        if(visited[i]==maxcount):
            result=i
    
    print(f"#{testcase} {result}")