# 12:25
# 12:52
# dfs 로 모든경우의수를 탐색하면서 최대일때를 구하면됨 함수의 인자로 현재상태와,깊이 2개를 필요로하고
# 깊이가 교환횟수 이면 종료하고 결과값에 현재상태와 비교해서 현재상태가 더크면 갱신
# 선택할수있는 경우가 탐색을해도 줄어들지않음 중복이 생길수있는데 중복을 허용함 문제에서
# 음 중복검사를 제외 해야할듯 시간이 오래걸린다

T=int(input())

for test_case in range(1,1+T):
    array,n=input().split()
    n=int(n)
    array=list(array)
    print(array)
    result=0
    visited=set()
    def dfs(current,depth):
        global result

        temp = ''.join(current)
        if(depth==n):

            temp=''.join(current)
            result=max(result,int(temp))
            return
        if((temp,depth) in visited):
            return
        else:
            visited.add((temp,depth))

        for i in range(len(array)):
            for j in range(i+1,len(array)):
                temp=current[i]
                current[i]=current[j]
                current[j]=temp
                dfs(current,depth+1)
                temp = current[i]
                current[i] = current[j]
                current[j] = temp

    dfs(array,0)

    print(f'#{test_case} {result}')
