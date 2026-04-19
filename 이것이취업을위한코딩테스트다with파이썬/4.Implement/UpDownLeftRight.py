size=int(input())
move=input().split()

coordinate=[1,1]


for count in range(len(move)):
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
        continue
print(coordinate)