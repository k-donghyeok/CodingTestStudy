#17:00
import sys

n,m = map(int,input().split())

array=list(map(int,sys.stdin.readline().split()))

start=0
end=max(array)
result=0
while(start<=end):
    middle=(start+end)//2
    total=0
    for i in array:
        if(i>middle):
            total+=i-middle
    
    if(total<m):
        end=middle-1
    else:
        result=middle
        start=middle+1
    
print(result)
    

        