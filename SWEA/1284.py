# 그냥 시키는대로 적으면될듯

T = int(input())

for test_case in range(1,T+1):
    p,q,r,s,w= map(int,input().split())

    a=p * w
    if(w<=r):
        b =q
    elif(w>r):
        b=(w-r)*s +q

    if(a>b):
        print(f'#{test_case} {b}')
    else:
        print(f'#{test_case} {a}')
