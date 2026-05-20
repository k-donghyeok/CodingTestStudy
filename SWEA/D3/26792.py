# 더했을때 a 뺏을때 b
# x+y =a , x-y=b 이닌까 x를 -100 부터 늘려가면서 해당하는 y 가 x-y =b 를 만족하는지
# 보면 될거같은데

T=int(input())

for test_Case in range(1,1+T):
    x,y =map(int,input().split())
    result=[]
    for a in range(-100,101):
        b=x-a
        if(a-y==b):
            result.append((x-b,a-y))
    #print(result)
    #print(f'#{test_Case}',end=' ')
    for i in result:
        print(f'{i[0]} {i[1]}')