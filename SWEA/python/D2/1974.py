# 행 검사 -> 열검사 -> 네모검사 ? for 3번?

T = int(input())

for test_case in range(1,T+1):

    array=[]
    for i in range(9):
        array.append(input().split())


    s=set()
    result=1
    #행검사
    for i in range(len(array)):
        for j in range(len(array)):
            s.add(array[i][j])

        if(len(s)<9):

            result=0
            s.clear()
            break
        s.clear()

    #열검사
    for i in range(len(array)):
        for j in range(len(array)):
            s.add(array[j][i])

        if (len(s) < 9):

            result = 0
            s.clear()
            break
        s.clear()
    #사각형 검사
    for i in range(0,9,3):
        for j in range(0,9,3):

            for k in range(i,i+3):
                for l in range(j,j+3):
                    s.add(array[k][l])

            if (len(s) < 9):
                result = 0
                s.clear()
                break
            s.clear()

    print(f'#{test_case} {result}')