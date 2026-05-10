# 음 그냥 반복문으로 바로 하면되나? 가지수가 많아지면 다르게
#해야할거같은데 n 이 적으닌까 그냥 바로하자

T=int(input())

for test_case in range(1,1+T):
    n=int(input())
    total=0
    for i in range(1,n+1):
        if(i%2==0):
            total-=i
        else:
            total+=i

    print(f'#{test_case} {total}')