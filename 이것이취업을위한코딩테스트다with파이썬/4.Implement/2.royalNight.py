location = input()

x=ord(location[0])
y=int(location[1])
result=0

moves=['UL','UR','DL','DR','LU','LD','RU','RD']
dx=[-1,1,-1,1,-2,-2,2,2]
dy=[-2,-2,2,2,-1,1,-1,1]


for move in range(len(moves)):
    nx=x+dx[move]
    ny=y+dy[move]
    if(nx<97 or nx >104 or ny<1 or ny>8):
        continue
    result+=1

print(result)


