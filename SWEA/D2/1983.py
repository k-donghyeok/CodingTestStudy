# 4 33
T=int(input())

for test_case in range(1,1+T):
    n,k = map(int,input().split())

    stuInfo=[]
    for i in range(n):
        stuInfo.append(list(map(int,input().split())))

    score={}
    for i in range(len(stuInfo)):
        total=stuInfo[i][0]*0.35 + stuInfo[i][1]*0.45 + stuInfo[i][2]*0.2
        score[i]=total

    #print(score)
    sortedScore = sorted(score.items(),key=lambda x:x[1], reverse=True)
    #print(sortedScore)

    result=[[]for _ in range(n)]
    temp=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    for i in range(len(sortedScore)):
        result[sortedScore[i][0]]=temp[i//(n//10)]
    #print(result)
    print(f'#{test_case} {result[k-1]}')


