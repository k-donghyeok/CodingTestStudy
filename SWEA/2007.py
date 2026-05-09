# 배열을 1칸 2칸 3칸 씩 크기를 늘려가면서
# 다음거랑 그전거랑 같은지 비교하다가 같은 크기일때찾기

#5 46

T = int(input())

for test_case in range(1,1+T):
    strinput=input()



        for length in range(1,len(strinput)):

            if(strinput[:length]==strinput[length:length*2]):
                print(f'#{test_case} {length}')

                break
