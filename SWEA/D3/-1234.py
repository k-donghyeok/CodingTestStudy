#3:00
#  배열에서 2칸을 뽑아서 서로 같은지 아닌지 검사를 하고
# 같으면 제거 인데 바로 제거하면 인덱스 관리 가 복잡할거같으니
# 제거해야하는 범위를 start finish 로 표시해두고
# 좌우가 다른 값이 나올때까지 범위를 확장시키고
# 다른값이 나왔다면 그떄 지울까 아니면 그냥 놔두고 다른 부분을 보러가야하나
# 음 근데 보닌까 회문 검사인데 길이가 짝수일때만 인거같은데
# 그럼 회문검사의 길이를 어떻게 설정하고 탐색을하지
# 2 4 6 8 이렇게 점점 늘리는방식으로?
# 4짜리 회문 하나 8짜리 회문하나 이렇게 2개가  있다면?
# 길이를 제일 최대에서 검사를 한다면 8짜리 를 찾고 4짜리 를 찾기위해 완탐을 해야하고
# 길이를 최소에서 시작한다면 2짜리 찾고 2짜리 찾을때 8짜리의 일부분이 찾아질거고
# 그때 제거를 한다면 만약에 길이가 4짜리 이면 2개 날려서 길이가 2 가되므로 누락이되네
# 음 최대길이로 완탐으로 탐색하면되려나?
# 문자열의 길이가 그렇게 길지 않으니 그렇게하자

for test_Case in range(1,11):
    n,array= input().split()

    n=int(n)
    array=list(array)
    #print(array)
    count=0
    while(count<n):
        for j in range(count+1):
            if((n-count) %2 ==1):
                maxLen=n-count-1
            else:
                maxLen=n-count
            for length in range(maxLen,1,-2):
                if(j + length <= len(array)):
                    if(array[j:j+length]==array[j:j+length][::-1]):
                        #print(count,j,length)
                        #print(array)
                        #print(array[j:j + length])
                        del array[j:j+length]
                        n-=2
                        count=0
        count+=1

    print(f'#{test_Case}',end=' ')
    for i in array:
        print(i,end='')
    print()



