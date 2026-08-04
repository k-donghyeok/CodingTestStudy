# 검은색 0 흰색1
from collections import deque

T= int(input())

for test_case in range(1,1+T):
    n,k = map(int,input().split())

    array=[]
    for i in range(n):
        array.append(input().split())



    def leftcheck(x,y):
        while(True):
            nx=x-1
            if(nx>=0 and nx<n and array[y][nx]=='1'):
                return False
            else:
                return True

    def downCheck(x,y):
        while (True):
            ny = y - 1
            if (ny >= 0 and ny < n and array[ny][x] == '1'):
                return False
            else:
                return True

    result=0
    for i in range(n):
        for j in range(n):
            if(array[i][j]=='1'):
                length=0
                if(leftcheck(j,i)):
                    x=j

                    while(x<n):

                        if(array[i][x]=='1'):
                            length += 1
                            x += 1
                        else:
                            break
                    if(length==k):
                        result+=1
                length=0
                if(downCheck(j,i)):
                    y = i
                    while (y < n ):

                        if(array[y][j]=='1'):
                            length += 1
                            y += 1
                        else:
                            break
                    if (length == k):
                        result += 1

    print(f'#{test_case} {result}')