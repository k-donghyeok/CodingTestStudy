# 12:30
# 12:40
# 탐색 유형문제 같고 일단 완탐 하면서 슬라이싱으로 범위 지정해서 검사하면 될거같음

for _ in range(1,11):
    n=int(input())
    target=input().rstrip()

    array=input().rstrip()
    result=0
   # print(target)
    for i in range(len(array)-len(target)+1):
        temp=array[i:i+len(target)]
        #print(array)
        #print(temp)
        if(temp==target):
            result+=1

    print(f'#{n} {result}')