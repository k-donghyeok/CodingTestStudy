size=int(input())
orders=input().split()

coordinate=[1,1]

# 처음 풀었을때
""" for count in range(len(move)):
    if(move[count]=='U'):
        coordinate[0]+=-1
        if(coordinate[0]<1):
            coordinate[0]+=1
        continue
    if(move[count]=='D'):
        coordinate[0]+=1
        if(coordinate[0]>size):
            coordinate[0]+=-1
        continue
    if(move[count]=='L'):
        coordinate[1]+=-1
        if(coordinate[1]<1):
            coordinate[1]+=1
        continue
    if(move[count]=='R'):
        coordinate[1]+=1
        if(coordinate[1]>size):
            coordinate[1]+=-1
        continue """


# dx dy 방식으로 풀어봤을때
x=1
y=1
move =['U','D','L','R']
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for order in orders:
    for count in range(len(move)):
        if(move[count]==order):
            nx=x+dx[count]
            ny=y+dy[count]
            if(nx<1 or ny<1 or nx>size or ny>size):
                continue
            x=nx
            y=ny

print(f"{x},{y}")