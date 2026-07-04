# 카운팅 방식 사용하면 되긴한데 이게 내가 문제를 보고 100프로 떠올린게 아니라
# 저번에 풀었을때 기억이 나서 그냥 문제를 보자마자 떠오른거라 좀 그렇네
# 카운팅 방식이 왜 필요한지 그게 순서대로 생각이 나야하는데
# 일단 음 원래는 정렬하고 최고점 갯수 구하고 최저점 갯수도 구하고 최고점이 많을때 최저점이 많을때 이렇게 나눠서 풀었는데
# 사실 그냥 배열에 카운팅방식으로 각각의 길이에 해당하는 갯수를 기록하고
# 최고점을 찾고 최저점을 찾고 최고점 갯수-1 최고점-1 길이의 갯수+1 인데 최고점 갯수가0이면 다음 최고점을 찾아야함
# 똑같이 최저점도 최저점 찾고 최저점 갯수-1 최저점+1 길이 갯수 +1 최저점 갯수가0이면 다음 최저점 찾아야함
# 이게 1번 덤프했을때 이루어져야할것들 입력받은 횟수만큼 반복하면 최종카운팅 배열이 나오고 반복문안에서 최고점 최저점 차이를
# 저장

# 1:16
# 1:37

for test_Case in range(1,11):
    n=int(input())

    array=[int(x) for x in input().split()]
    counting=[0 for _ in range(101)]
    for i in array:
        counting[i]+=1
    maxLen=max(array)
    minLen=min(array)
    for i in range(n):
        while (counting[maxLen] == 0):
            maxLen -= 1
        while (counting[minLen] == 0):
            minLen += 1

        if(maxLen-minLen<=1):
            break

        if(counting[maxLen]>0):
            counting[maxLen]-=1
            counting[maxLen-1]+=1



        if (counting[minLen] > 0):
            counting[minLen] -= 1
            counting[minLen + 1] += 1

    while (counting[maxLen] == 0):
        maxLen -= 1
    while (counting[minLen] == 0):
        minLen += 1


    print(f'#{test_Case} {maxLen-minLen}')