# while 문으로 n 을 곱하면서 곱한 값을 set에 넣어서 set의 길이가 10이면 중단

T=int(input())

for test_case in range(1,1+T):

    n=input().rstrip()
    s=set()
    count=1
    cal=0
    for i in n:
        s.add(int(i))

    while(len(s)<10):
        n=int(n)
        count += 1
        cal=n*count
        cal=str(cal)
        for i in cal:
            s.add(int(i))



    print(f'#{test_case} {cal}')
