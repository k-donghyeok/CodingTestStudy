# 트리를 써야할거같은데 음
# 입력이 깊이가 되고 각 노드는 자식을 2개 가진다 근데 인접한 자식은 공유를 한다
# 일단 트리를 어떻게 만들지 배열로 만들어야하나?
# 2차원 배열의 y 를 깊이로 x를 너비로 해서 만들면되나?

T=int(int(input()))

for test_case in range(1,1+T):
    n= int(input())

    array=[[0]*i for i in range(1,n+1)]
    array[0][0]=1


    for i in range(1,n):
        for j in range(i+1):
            if(j>0 and j<i):
                array[i][j]=array[i-1][j-1] + array[i-1][j]
            if(j==i):
                array[i][j] = array[i - 1][j - 1]
            if(j==0):
                array[i][j] = array[i - 1][j]
    print(f'#{test_case}')
    for i in array:
        for j in i:
            print(j,end=' ')
        print()
