# 2:45
# 2:54
# 가로 세로 2방향만 검사하면되고 길이가 주어지네 완탐으로  길이만큼 잘라서 검사하면될듯

for test_case in range(1,11):
    n= int(input())

    array=[]
    for y in range(8):
        array.append(input().rstrip())

    result=0
    #행
    for y in range(8):
        for x in range(8-n+1):
            temp=array[y][x:x+n]
            if(temp==temp[::-1]):
                result+=1

    #열
    for x in range(8):
        for y in range(8-n+1):
            temp=''
            for k in range(n):
                temp=temp+''.join(array[y+k][x])

            if(temp==temp[::-1]):
                result += 1

    print(f'#{test_case} {result}')