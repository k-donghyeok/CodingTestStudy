#열을 넘어가면서 탐색을 해야할거같음
# 열에 2개 이상이면?
# 1n 2s
for test_case in range(1,11):
    length=int(input())
    array=[]
    for i in range(length):
        array.append(input())

    for i in range(length):
        for j in range(length):
            if(array[i][j]==1):
                if(i+1<length)
