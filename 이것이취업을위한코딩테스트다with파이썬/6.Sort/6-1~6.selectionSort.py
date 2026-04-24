# 선택정렬 seletionSort
array=[7,5,9,0,3,1,6,2,4,8]

def selectionSort(array):
    for i in range(len(array)):
        for j in range(i,len(array)):
            if(array[j]<=array[i]):
                array[i],array[j]=array[j],array[i]
    



# 삽입정렬 insertionSort

def insertionSort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if(array[j]<array[j-1]):
                array[j-1],array[j]=array[j],array[j-1]

# 퀵 정렬 quckSort

def quckSort(array,start,end):
    if(start>=end):
        return 
    pivot = start
    left =start+1
    right =end

    while (left<=right):
        
        while(left <=end and array[left] <=array[pivot]):
            left+=1
        
        while(right >start and array[right] >=array[pivot]):
            right-=1



        if(left>right):
            array[pivot],array[right]=array[right],array[pivot]
            
        else:
            array[left],array[right]=array[right],array[left]

    quckSort(array,start,right-1)
    quckSort(array,right+1,end)


# 계수 정렬 countSort
def countSort(array):
    maxNum= max(array)
    temp = [0 for _ in range(maxNum+1)]
    for i in range(len(array)):
        temp[array[i]]+=1

    for i in range(len(temp)):
        for j in range(temp[i]):
            print(f"{i}",end=' ')

array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
countSort(array)