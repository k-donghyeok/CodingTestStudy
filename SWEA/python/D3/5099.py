# 10:20

# 음 배열 의 삭제 삽입 구현 문제같은데
# while 문으로 화덕안에 피자가 없을때까지 반복시켜서
# 화덕안의 치즈를 //2 해주고 0이면 삭제시키고 그다음 피자를 삽입
from collections import  deque

T=int(input())

for test_Case in range(1,1+T):
    n,m =map(int,input().split())

    temp=[int(x) for x in input().split()]
    pizza=deque()
    for i in range(m):
        pizza.append([i,temp[i]])
    fireDuck=deque()
    for i in range(n):
        fireDuck.append(pizza.popleft())
    while(fireDuck):
        pizzaNumber,cheeze=fireDuck.popleft()
        if(cheeze//2>0):
            fireDuck.append([pizzaNumber,cheeze//2])
        else:
            if(pizza):
                fireDuck.append(pizza.popleft())
            elif(not fireDuck):
                print(f'#{test_Case} {pizzaNumber+1}')





