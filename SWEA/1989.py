# 회문검사 문자열 길이 /2 만큼 반복해서 첫번째랑 마지막 두번쨰랑 마지막-1 이렇게 검사

T= int(input())

for test_case in range(1,1+T):
    string = input().rstrip()

    count=len(string)//2
    result=1 # 1이면 회문 0이면 회문아님
    for i in range(count):
        print(f'{string[i]} {string[len(string)-1-i]}')
        if(string[i]!=string[len(string)-1-i]):
            result=0
            break

    print(f'#{test_case} {result}')

# 파이썬은 슬라이싱 으로 [::-1] 해서 문자열 이랑 같은지 아닌지 검사해도됨
# if(string==string[::-1]) 