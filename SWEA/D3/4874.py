#숫자는 스택에 넣는다.

#연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.

#‘.’은 스택에서 숫자를 꺼내 출력한다.

from collections import  deque
T=int(input())

for test_case in range(1,1+T):
    array=list(input().split())

    stack=deque()
    for i in array:
        if(i=='+'):
            if(len(stack)>=2):
                a=stack.pop()
                b=stack.pop()
                stack.append(b+a)
            else:
                result='error'
                break
        elif(i=='-'):
            if (len(stack) >= 2):
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            else:
                result = 'error'
                break
        elif (i == '*'):
            if (len(stack) >= 2):
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            else:
                result = 'error'
                break
        elif (i == '/'):
            if (len(stack) >= 2):
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)
            else:
                result = 'error'
                break
        elif(i == '.'):
            if(len(stack)==1):
                result=stack.pop()
                break
            else:
                result='error'
                break
        else:
            stack.append(int(i))

    print(f'#{test_case} {result}')

