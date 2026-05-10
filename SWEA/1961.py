# 음 2차원배열을 방향을 돌려야한다
# 시계방향 90도 회전시 첫번째 열의 마지막 요소 부터 차례로 넣으면된다


T=int(input())

for test_case in range(1,T+1):
    n=int(input())
    array=[]
    result=[]
    temp=[[0]*n for _ in range(n)]
    count=0
    for row in range(n):
        array.append(list(map(int,input().split())))

    def change(before,after):
        global count
        if(count==3):
            return

        for i in range(n):
            for j in range(n):
                after[i][n-1-j]=before[j][i]
        result.append(after)
        count+=1
        before=[[0]*n for _ in range(n)]
        change(after,before)

    change(array,temp)
    print(result)
    print(f'#{test_case}')
    # for i in range(n):
    #     for j in range(n):
    #         print(f'{result[0][i][j]}',end='')
    #     print(' ',end='')
    #     for j in range(n):
    #         print(f'{result[1][i][j]}',end='')
    #     print(' ',end='')
    #     for j in range(n):
    #         print(f'{result[2][i][j]}',end='')
    #     print()

    for i in range(n):
        print(''.join(map(str,result[0][i])),
              ''.join(map(str,result[1][i])),
              ''.join(map(str,result[2][i])))
