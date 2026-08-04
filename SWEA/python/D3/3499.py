# 3:00
# 3:13


# 음 어떻게 하면될까 일단 배열에 넣고
# 슬라이싱으로 절반을 잘라야겠지? 중간값은 홀수이면 왼쪽이1더크게
# 그다음 잘라진 2개를 한번씩 추가할까 새로운 배열에 그럼 될거같은데?
# 그리고 배열 출력
# 이걸로도 충분히 구현될거같은데

T=int(input())

for test_Case in range(1,1+T):
    n=int(input())

    array=[x for x in input().split()]
    if(len(array)%2==1):
        middle = (len(array) // 2)+1
    else:
        middle = (len(array) // 2)
        # len=5 middle=3
        # 1 2 3 4 5
    left=array[:middle]
    right=array[middle:len(array)]
    result=[]

    for i in range(len(right)):
        result.append(left[i])
        result.append(right[i])
    if(len(array)%2==1):
        result.append(left[-1])

    print(f'#{test_Case}',end=' ')
    for _ in result:
        print(f'{_}',end=' ')
    print()
