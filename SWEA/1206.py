# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1




for test in range(1,11):

    count =int(input())

    building = []
    sum=0
    temp=map(int,input().split())
    for i in temp:

        building.append(i)


    for i in range(2,count-2):
        calBuilding=building[i-2:i+3] #계산되는 빌딩들
        calBuilding.sort()
        if(calBuilding[-1]==building[i]):
            sum+=building[i]-calBuilding[-2]

    print(sum)



