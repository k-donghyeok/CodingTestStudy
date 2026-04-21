rowSize,colSize=map(int,input().split())
x,y,direction=map(int,input().split())
locationInfo=[]
passedLocation=[]
turnCount=0
count=1

passedLocation=[[0]* colSize for i in range(rowSize)]

for row in range(rowSize):
    locationInfo.append(list(map(int,input().split())))
    
passedLocation[x][y]=1


dx=[-1,0,1,0]  #북 동 남 서
dy=[0,1,0,-1]

while True:
    direction-=1
    turnCount+=1
    if(direction==-1):
        direction=3

    nx=x+dx[direction]
    ny=y+dy[direction]
    if(( nx>=0 and nx<rowSize ) and (ny>=0 and ny<colSize )):
        if(locationInfo[nx][ny]==0 and passedLocation[nx][ny]==0):
            x=nx
            y=ny
            turnCount=0
            passedLocation[x][y]=1
            count+=1
            continue
    
    
    
    if(turnCount==4):
        if(locationInfo[x-dx[direction]][y-dy[direction]]==0):
            x=x-dx[direction]
            y=y-dy[direction]
            turnCount=0
        else:
            break

print(count)

    

    
    
    
    
    

