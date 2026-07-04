#11:31
#12:05
# 0 1 2 3 4 5 6 7 8 9
# 1 2 3 8 0 9 9 0 8 4

# 0 1 2 3 4 5 6 7 8 9
# 1 2 3 8 0 0 8 4

# 0 1 2 3 4 5 6 7 8 9
# 1 2 3 8 8 4

# 길이 2로 탐색해서 같으면 소거하고 탐색 start를 -1 함
# dx 로 인덱스 관리를 해야겠는데 반복문으로는 다시 돌리기가 힘들어
# start가 길이 -2 이면 종료
dx=[-1,1] # 좌 우
for test_Case in range(1,11):
    n,array= input().split()
    array=list(array)
    #n=int(n)
    #print(array)
    nx=0

    while(nx<len(array)-1):
        temp=array[nx:nx+2]
        #print(temp,nx)
        if(temp==temp[::-1]):
            for j in range(2):
                array.pop(nx)
            nx = nx + dx[0]
            if(nx<0):
                nx=0

        else:
            nx = nx + dx[1]




    print(f'#{test_Case}',end=' ')
    for i in array:
        print(f'{i}',end='')
    print()
