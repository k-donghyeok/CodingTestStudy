# [실전 문제] 큰 수의 법칙
#
# 개요:
# - N개의 자연수로 이루어진 배열이 주어진다.
# - 이 중에서 M번 숫자를 더하여 만들 수 있는 가장 큰 값을 구한다.
# - 단, 같은 인덱스(같은 원소)의 수는 연속해서 K번을 초과하여 더할 수 없다.
# - 서로 다른 인덱스의 값이 같더라도, 인덱스가 다르면 다른 수로 취급한다.
#
# 입력:
# - 첫째 줄: N, M, K (N: 배열 크기, M: 더하는 횟수, K: 연속 제한)
# - 둘째 줄: N개의 자연수 (공백 구분)
#
# 출력:
# - 규칙을 적용해 M번 더했을 때의 최댓값을 출력
#
# 조건:
# - 2 <= N <= 1000
# - 1 <= M <= 10000
# - 1 <= K <= 10000
# - 각 수는 1 이상 10000 이하
# - K는 항상 M보다 작거나 같다 (K <= M)
#
# 예시:
# 입력:
# 5 8 3
# 2 4 5 4 6
# 출력:
# 46
#
# 설명(예시):
# - 가장 큰 수 6을 연속 3번까지 더할 수 있으므로
#   6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46


#2025-12-28-17:02 시작 
#2025-12-28-17:25 시작 

inputInfo = input().split(' ')
numberList = input().split(' ')
sum=0
count=0
sortedNumber = sorted(numberList,reverse=True)
print(sortedNumber)
for i in range(int(inputInfo[1])):
    count+=1
    if count==int(inputInfo[2]):
        sum+=int(sortedNumber[1])
        count=0
        continue
    
    sum+=int(sortedNumber[0])

print(sum)