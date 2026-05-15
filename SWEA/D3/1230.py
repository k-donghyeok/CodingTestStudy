# 7:49
# 배열에 암호문들 넣고 명령어들도 배열에 넣고
# 명령어 배열들에서 하나씩 꺼내면서 해당하는 명령 실행


for test_case in range(1,11):
    n=int(input())
    array=[x for x in input().split()]

    m=int(input())
    orders=[x for x in input().split()]

    order=['I','D','A']

    for i in range(len(orders)):
        if(orders[i] in order):
            if(orders[i]=='I'):
                for j in range(int(orders[i+2])):
                    array.insert(int(orders[i+1])+j,orders[i+3+j])
            elif(orders[i] == 'D'):
                for j in range(int(orders[i+2])):
                    array.pop(int(orders[i+1]))
            elif(orders[i] == 'A'):
                for j in range(int(orders[i+1])):
                    array.append(orders[i+2+j])

    print(f'#{test_case}',end=' ')
    for i in range(10):
        print(array[i],end=' ')
    print()