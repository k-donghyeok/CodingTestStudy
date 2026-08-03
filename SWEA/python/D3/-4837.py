# 5:25

# 일단 부분집합을 먼저 만들어야해

# 123 124 125 126 127
# 이걸 만족하는 규칙을 찾아야해

# 일단 길이가 n인 배열을 만드닌까 n번 반복하는데
# 음 반복문의 깊이가 n이어야하나?
# 자릿수마다 값을 인덱스로 조절하면서 탐색해야하나?
# 음 그럼 재귀를 사용해야할거같은데

# 아니면 1부터 12까지 스택에서
# 갑을 꺼내면서 백트레킹인가>
# 백트레킹 한다하면 값을 꺼낸다 안꺼낸다
# 종료조건은 n번 깊이까지 왔거나 원소 합이 k 인 경우
# 음 다시 부분집합 1, 2, 3, 4 갯수가 1개에서 n개 까지 생기고
# 12 13 14 15 반복하는 횟수를 늘려줘야하나
# 1234567 1234568 1234569 1234576 1234578 1234579
# 1 2
# 이거 무조건 dfs 백트레킹이다
# 값을 선택했을때 안했을때 선택할때마다 누적합이 k 인지 검사하고 k이면 최종결과에 더하기1
# 내가 뭘 선택했는지를 들고가야하나 그리고 누적합
# visited 로 1부터 12까지 만들고 선택하면 해당 인덱스 값을 1로 바꾸자
T=int(input())

for test_case in range(1,1+T):
    n,k = map(int,input().split())
    nums=[0 for x in range(13)]
    #print(nums)
    result=0
    def dfs(start,sum,depth,visited):
        global result
        if(sum==k and depth==n):
            result+=1
            return
        if(depth>n):
            return
        for index in range(start,13):
            if(visited[index]==0):
                visited[index]=1
                dfs(index+1,sum+index,depth+1,visited)
                visited[index] = 0

    dfs(1,0,0,nums)
    print(f'#{test_case} {result}')
