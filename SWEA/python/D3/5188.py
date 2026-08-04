# 3:51
# 4:22
# 음 2차원 배열에 선택을 한다 안한다로 내 상태가 변경가능하고
# 백트레킹에 dfs 사용

# 선택한다 안한다로 재귀함수 호출부분을 2개 만들고
# 오른쪽 아래 두개가는경우를 반복문으로 2번 가도록만들고
# 그럼 함수의 인자로 합계, 방문기록은 필요없을듯
# 방문기록이 필요없으면 백트레킹이 아닌가? 일단
# 종료조건 좌표가 오른쪽 끝에 도달했을때 좌표도 인자로 필요할듯
# 아 선택한다 안한다가 아니라 그냥 무조건 선택이구나
# 음 시간이 초과되었다 종료조건으로 현재 합계가 결과보다 크면 바로 종료
T=int(input())

for test_Case in range(1,1+T):
    n=int(input())
    array=[]
    for _ in range(n):
        array.append(input().split())
    dx=[1,0] #우 하
    dy=[0,1]
    result=99999
    def dfs(x,y,sum):
        global result
        if(sum>result):
            return
        if(x==n-1 and y==n-1):
            result=min(result,sum)
            return

        for i in range(2):
            nx=x+dx[i]
            ny=y+dy[i]

            if(nx>=0 and nx<n and ny>=0 and ny<n):
                dfs(nx,ny,sum+int(array[ny][nx]))

    dfs(0,0,int(array[0][0]))
    print(f'#{test_Case} {result}')