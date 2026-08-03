#11:14

# while 문으로 3으로 나눈 몫이 1 이상이면 현재값에서 3을 빼고 결과값에 1을 더한다 다시반복한다
# 아닌데 그냥 3으로 나눈 몫 출력하면되는데

T=int(input())

for test_Case in range(1,1+T):

    n=int(input())

    print(f'#{test_Case} {n//3}')

