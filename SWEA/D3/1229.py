# 2:37

#배열을 만들고 입력을 넣어서 나오는 문자에따라 해당하는 행동을 해준다
# 완전탐색

for test_case in range(1,11):
    arrayLen=int(input())

    array=[x for x in input().split()]

    ordersLen=int(input())

    orders=[x for x in input().split()]
    #print(orders)
    for i in range(len(orders)):
        if(orders[i]=='I'):
            for j in range(int(orders[i+2])):
                array.insert(int(orders[i+1])+j,orders[i+3+j])
        elif(orders[i]=='D'):
            for j in range(int(orders[i+2])):
                array.pop(int(orders[i+1]))

    print(f'#{test_case}',end=' ')
    for i in range(10):
        print(array[i],end=' ')
    print()