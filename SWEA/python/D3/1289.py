# 입력을 리스트에 넣은다음  완전탐색으로 1인지 아닌지 검사

T=int(input())

for test_case in range(1,1+T):
    array=input()
    temp=['0' for _ in range(len(array))]
    count=0
    for i in range(len(array)):
        if(array[i]!=temp[i]):
            temp[i:]=[array[i] for _ in range(len(temp)-i)]
            count+=1



    print(f'#{test_case} {count}')