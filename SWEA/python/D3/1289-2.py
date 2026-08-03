# 7:34
# 7:57
# 음 초기값 이랑 입력 값이랑 비교하면서 다르면 횟수 +1 하고 입력값을 변경
# 해서 완탐하면 될거같은데

T=int(input())

for test_Case in range(1,1+T):

    array=[int(x) for x in input().rstrip()]
    #print(array)
    result=0
    temp=[0 for _ in range(len(array))]

    for i in range(len(array)):
        if(array[i]!=temp[i]):
            if(temp[i]==0):
                result+=1
                for j in range(i,len(array)):
                    temp[j]=1
            else:
                result += 1
                for j in range(i, len(array)):
                    temp[j] = 0



    print(f'#{test_Case} {result}')