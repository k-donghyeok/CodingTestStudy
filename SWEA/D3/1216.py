# 2:38
# 3:29
# 회문의 길이를 저장하면서 길이만큼의 배열을 회문검사?
# 긴 길이를 구하는거닌까 최대길이에서 1씩 감소하면서 회문검사 하자
# [::] 로 검사할 부분 잘라서 검사하기 그래서 회문을 찾으면 그떄가 가장긴 회문
# 길이가 나올때마다 max 로 최댓값 갱신
# 다시 가보자이
# 3:49
# 일단 잘라서 검사는 맞고 회문의 길이로 반복문을 돌리자
for test_Case in range(1,11):

    n=int(input())

    array=[]
    result=0
    for i in range(100):
        array.append(input().rstrip())
    stop=False
    for maxlen in range(100,0,-1):
        #가로
        for i in range(100):
            for j in range(0,101-maxlen):
                temp=array[i][j:j+maxlen]
                for k in range(len(temp)//2):
                    if(temp[k]!=temp[-k-1]):
                        break
                    else:
                        if(k==(len(temp)//2)-1):
                            result=maxlen
                            stop=True
                if(stop):
                    break
            if(stop):
                break
        if(stop):
            break

        #세로
        for i in range(100):
            for j in range(0,101-maxlen):
                temp=''.join(array[k][i] for k in range(j,j+maxlen))
                for k in range(len(temp)//2):
                    if(temp[k]!=temp[-k-1]):
                        break
                    else:
                        if(k==(len(temp)//2)-1):
                            result=maxlen
                            stop=True

                if(stop):
                    break
            if (stop):
                break
        if (stop):
            break

    print(f'#{n} {result}')