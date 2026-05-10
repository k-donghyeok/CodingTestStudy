# 12:55

for _ in range(1,11):
    test=int(input())
    array=[]
    rowSum=0
    colSum=0
    colMax=0
    rowMax=0
    rightDownSum=0
    leftDownSum=0
    for _ in range(100):
        array.append(list(map(int,input().split())))
    
    for i in range(100):
        colSum=0
        rowSum=0
        rightDownSum+=array[i][i]
        leftDownSum+=array[-i-1][-i-1]
        for j in range(100):
            colSum+=array[i][j]
            rowSum+=array[j][i]
            
        
        
        if(colMax<colSum):
            colMax=colSum
        if(rowMax<rowSum):
            rowMax=rowSum
        
    
    print(f"#{test} {max(colMax,rowMax,rightDownSum,leftDownSum)}")
