#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1


T = int(input())

for test_case in range(1,T+1):
    price=[]
    dayCount=int(input())
    temp=map(int,input().split())

    for _ in temp:
        price.append(_)
    startindex=0
    maxindex=0
    result=0

    while(startindex<dayCount-1):
        
        for i in range(startindex+1,dayCount):
            if(price[maxindex]<price[i]):
                maxindex=i
        for i in range(startindex,maxindex+1):
            result+=(price[maxindex]-price[i])
        if(startindex<=maxindex):
            startindex=maxindex+1
            maxindex=startindex
        else:
            startindex+=1
        

        
        
                

    print(f"#{test_case} {result}")
