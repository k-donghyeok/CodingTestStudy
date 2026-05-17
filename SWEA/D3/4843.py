# 3:24
# 3:40

# 입력을 배열에 저장후 한번 정렬하고 반복문으로 i 를 증가시키면서 i 한번 출력 -i-1 출력
# 반복문은 입력받은 배열의 길이의 절반만큼 길이가 짝수면 괜찮지만 홀수면
# 반복문 다돌고 마지막에 한번더 출력해줘야함

T=int(input())

for test_case in range(1,1+T):
    n=int(input())

    array=[int(x) for x in input().split()]
    array.sort(reverse=True)
    print(f'#{test_case}',end=' ')
    for i in range(5):
        print(f'{array[i]} {array[-i-1]}',end=' ')
        if(len(array)%2 == 1):
            if (i == (len(array) // 2) - 1 ):
                print(f'{array[i + 1]}')
                break
    print()

