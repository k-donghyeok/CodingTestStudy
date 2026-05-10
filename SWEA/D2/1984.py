# 입력 받으면서 최대 최소 수를 구해놓고 입력받은 값을 리스트에 저장
# 최대 최소 뺀 것들의 평균 구ㅠ하기

T=int(input())

for test_case in range(1,1+T):

    array=list(map(int,input().split()))

    maxnum=max(array)
    minnum=min(array)

    array.remove(maxnum)
    array.remove(minnum)
    total=0
    for i in array:
        total+=i
    evg=total/len(array)
    evg=round(evg)
    print(f'#{test_case} {evg}')