T =int(input())

def search(num,curCount):
    global answer
    if(curCount==count):
        answer = max(answer, int(num))
        return
    
    num=list(num)
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            
            
            

            temp=num[i]   # 123 -> 213  i=0 j=1
            num[i]=num[j]
            num[j]=temp
           
            
            next_num = ''.join(num)
            if next_num not in visited[curCount + 1]:
                visited[curCount + 1].add(next_num)
                search(next_num, curCount + 1)
            temp=num[i]   # 213 -> 123  i=0 j=1
            num[i]=num[j]
            num[j]=temp
            

for test_case in range(1,T+1):
    
    num,count = input().split()
    count=int(count)
    answer=0
    
    visited=[set() for I in range(count+1)]
    visited[0].add(num)
    search(num,0)
    
 
    print(f"#{test_case} {answer}")

        
    
    