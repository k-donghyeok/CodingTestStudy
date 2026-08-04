# 3:27
# 4:06

# 2차원 배열에 암호문을 넣고 명령어에 맞게 삽입해준다
#그리고 2차원 배열에서 10개를 꺼내서 출력한다

for test_case in range(1,11):
    n=int(input())

    array=[x for x in input().split()]


    orderCount=int(input())

    orders=[x for x in input().split()]
    #print(orders)
    for i in range(len(orders)):
        if(orders[i]=='I'):
            index=int(orders[i+1])
            length=int(orders[i+2])
            temp=''
            for j in range(length):
                temp=temp+orders[i + 3+j]+' '
            #print(temp)
            #print(array)
            for k in range(len(list(temp.split()))):
                array.insert(index+k,list(temp.split())[k])

    print(f'#{test_case}',end=' ')
    for i in range(10):
        print(''.join(array[i]),end=' ')
    print()

