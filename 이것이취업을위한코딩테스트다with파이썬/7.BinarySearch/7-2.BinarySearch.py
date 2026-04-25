array=[0,2,4,6,8,10,12,14,16,18]
count=0

def binarySearch(array,start,end,target):
    
    
    
    middle=(end//2)+start
    if(array[middle]>target):
        return binarySearch(array,0,middle,target)
    elif(array[middle]<target):
        return binarySearch(array,middle,end,target)
    else:
        return middle

target=int(input('찾고자 하는 숫자를 입력하세요:'))
array=list(map(int,input('배열을 입력하세요:').split()))
print(f"{target}은 배열의 {binarySearch(array,0,len(array)-1,target)}번째 인덱스에 있습니다") 