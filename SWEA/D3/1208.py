for test_Case in range(1,11):
    n=int(input())

    array=[int(x) for x in input().split()]

    height=[0 for _ in range(101)]

    #print(height)

    for i in array:
        height[i]+=1

    max_h=max(array)
    min_h=min(array)
    while(n>0):
        n-=1
        height[max_h]-=1
        height[max_h-1]+=1

        height[min_h]-=1
        height[min_h+1]+=1

        while(height[max_h]==0):
            max_h-=1
        while(height[min_h]==0):
            min_h+=1

    print(f'#{test_Case} {max_h-min_h}')



