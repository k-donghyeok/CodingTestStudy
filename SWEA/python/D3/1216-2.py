# 5:09
# 5:57
# 2차원 배열을 탐색하는 문제 회문의 길이를 최대에서 줄여가는 방향으로
# 만약에 길이가 지금까지 찾은 회문의 길이보다 적다면 탈출

for _ in range(1,11):
    test_Case =int(input())

    array=[]
    for i in range(100):
        array.append(input().rstrip())

    result=0
    for i in range(100):
        for length in range(100,0,-1):
            #가로
            if(length<=result):
                break
            for j in range(101-length):
                temp=array[i][j:j+length]

                if(temp==temp[::-1]):
                    #print(temp)
                    result=max(result,length)
                temp =''
            #세로
                for k in range(length):
                    temp=temp+''.join(array[j+k][i])
                    #print(temp)

                if(temp == temp[::-1]):
                     #print(temp)
                     result = max(result,length)

    print(f'#{test_Case} {result}')