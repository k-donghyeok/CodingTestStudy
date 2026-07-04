for test_Case in range(1,11):

    n=int(input())

    array=[x for x in input().split()]

    m=int(input())

    orders=[x for x in input().split()]
    #print(array)
    #print(orders)
    for order in range(len(orders)):
        if(orders[order]=='I'):
            for i in range(int(orders[order+2])):
                array.insert(int(orders[order+1])+i,orders[order+3+i])
        elif(orders[order]=='D'):
            for i in range(int(orders[order+2])):
                array.pop(int(orders[order+1]))
        elif(orders[order]=='A'):
            for i in range(int(orders[order+1])):
                array.append(orders[order+2+i])

    print(f'#{test_Case}',end=' ')
    for i in range(10):
        print(f'{array[i]}',end=' ')
    print()