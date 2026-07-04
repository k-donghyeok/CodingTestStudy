# 8:02
# 8:17
# 길이를 줄여가면서 탐색 완탐
# 가로 세로 따로  길이가 n 이면 탐색 횟수는 범위 len-n+1


for _ in range(1,11):
    test_case =int(input())

    array=[]
    for y in range(100):
        array.append(input().rstrip())

    result=0
    for y in range(100):
        for length in range(100,0,-1):
            for x in range(100-length+1):
                temp=array[y][x:x+length]
                if(temp==temp[::-1]):
                    result=max(result,length)

    for x in range(100):
        for length in range(100,0,-1):

            for k in range(100-length+1):
                temp = ''
                for y in range(k,k+length):
                    temp=temp+''.join(array[y][x])
                if(temp==temp[::-1]):
                    result=max(result,length)

    print(f'#{test_case} {result}')
