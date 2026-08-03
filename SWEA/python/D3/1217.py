# 12:43
# 12:50

#  음 n,m ,result 3개를 인자로 절달해주면서 곱하면 되겠는데? 종료조건은 m번했을때

for _ in range(1,11):
    test_case=int(input())

    n,m=map(int,input().split())

    def cal(n,countt,result):
        if(countt==m):
            return result
        result*=n
        return cal(n,countt+1,result)

    print(f'#{test_case} {cal(n,0,1)}')

