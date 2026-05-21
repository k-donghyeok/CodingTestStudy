row,col = map(int,input().split())
minNumberOfRow=[]
colNumber={}
for row in range(1,row+1):
    colNumber[row]=map(int,input().split())
for row in range(1,row+1):
    temp=colNumber[row]
    minNumberOfRow.append(min(temp))
print(max(minNumberOfRow))

