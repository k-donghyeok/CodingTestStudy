# 데이터의 갯수가 많거나 탐색범위가 클경우 input() 사용시 동작속도가 느리다
#이럴때 sys 라이브러리의 readline() 사용하면 속도가 빠르다

import sys
input_data=list(map(int,sys.stdin.readline().split()))

for i in input_data:
    print(f"{i+1}",end=' ')