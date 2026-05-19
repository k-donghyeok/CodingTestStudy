# 5:03
T=int(input())

for _ in range(1,1+T):
    test_case=int(input())

    temp=[int(x) for x in input().split()]
    array=[0 for _ in range(101)]
    for i in temp:
        array[i]+=1

    maxNum=max(array)
    result=0
    for i in range(len(array)):
        if(array[i]==maxNum):
            result=i
    print(f'#{test_case} {result}')