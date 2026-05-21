array=[0,2,4,6,8,10,12,14,16,18]
count=0

def binarySearch(array,start,end,target):
    if(start>end):
        return -1
    
    
    middle=(end+start)//2
    if(array[middle]>target):
        return binarySearch(array,start,middle-1,target)
    elif(array[middle]<target):
        return binarySearch(array,middle+1,end,target)
    else:
        return middle

target=int(input('찾고자 하는 숫자를 입력하세요:'))
array=list(map(int,input('배열을 입력하세요:').split()))
result=binarySearch(array,0,len(array)-1,target)
if(result==-1):
    print(f"{target}은 배열에 존재하지 않습니다") 
else:
    print(f"{target}은 배열의 {result}번째 인덱스에 있습니다") 