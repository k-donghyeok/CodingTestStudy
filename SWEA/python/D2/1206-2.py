# 완전탐색? 기준을 1씩 증가시키면서 좌2 우2 범위에 기준보다 큰게있나 검사
# 중복 검사가 이뤄지긴함 근데 중복을 줄이는 방법이 떠오르지않음
# 일단 완탐ㄱㄱ

for test_case in range(1,11):
    n=int(input())
    array=list(map(int,input().split()))

    total=0
    for i in range(2,len(array)-2):
        result=255
        temp=array[i - 2:i + 3]
        for j in range(len(temp)):
            if(j==2):
                continue
            if(array[i] - temp[j]<=0):
                result=0
                break
            else:
                current=array[i] - temp[j]
            result=min(result,current)

        total+=result

    print(f'#{test_case} {total}')