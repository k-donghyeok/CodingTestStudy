T =int(input())

for test_case in range(1,T+1):
    num,count = input().split()
    numList=[]
    
    count=int(count)
    
    max=0
    maxIndex=0
    isSAME=False
    sameValue=-1
    sameIndex=[]
    for i in num:
        numList.append(int(i))
        
    
    for i in range(count):
        for j in range(i,len(numList)):
            if(numList[j]>=max):
                if(numList[j]==max):
                    isSAME=True
                    sameValue=numList[j]
                    print(f"sameVale={sameValue}")
                max=numList[j]
                maxIndex=j
        if(len(numList)-i>2):
            temp=numList[i]
            numList[i]=numList[maxIndex]
            numList[maxIndex]=temp
            continue
        elif(len(numList)-i<=2 and isSAME):
            for k in range(len(numList)):
                if(numList[k]==sameValue):
                    sameIndex.append(k)
                    print(f"sameIndex={sameIndex}")
            temp=numList[sameIndex[0]]
            numList[sameIndex[0]]=numList[sameIndex[1]]
            numList[sameIndex[1]]=temp
            continue
        else:
            temp=numList[-1]
            numList[-1]=numList[-2]
            numList[-2]=temp

    print(f"#{test_case} {numList}")

        
    
    