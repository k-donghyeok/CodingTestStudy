for test_case in range(1,11):
    length=int(input())
    array=[]
    for i in range(8):
        array.append(input())
    sum=0
    for i in range(8):
        for j in range(0,8-length+1):
            for k in range(length//2):
                if(array[i][j+k]!=array[i][j+length-1-k]):
                    break

                if(k==length//2-1):
                    sum+=1

    for i in range(8):
        for j in range(0,8-length+1):
            for k in range(length//2):
                if(array[j+k][i]!=array[j+length-1-k][i]):
                    break

                if(k==length//2-1):
                    sum+=1

    print(f'#{test_case} {sum}')