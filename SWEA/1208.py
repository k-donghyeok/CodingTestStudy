for test in range(1,2):
    
    count=int(input())
    boxList=list(map(int,input().split()))

   

    sortBoxList=sorted(boxList)
    
    while(count>0):
        if(max(sortBoxList)-min(sortBoxList)==0):
            break

        print(f"{count} {max(sortBoxList)} {min(sortBoxList)}")
        indexleft=1
        while(sortBoxList[indexleft-1]==sortBoxList[indexleft]):
            indexleft+=1
            
        indexRight=1
        for i in range(indexleft):
            if count==0:
                break
            if(sortBoxList[-indexRight-1]==sortBoxList[-indexRight]):
                sortBoxList[i]+=1
                sortBoxList[-indexRight]-=1
                count-=1
                indexRight+=1
            else:
                sortBoxList[i]+=1
                sortBoxList[-indexRight]-=1
                count-=1
                indexRight=1
                
            

        sortBoxList=sorted(sortBoxList)
    print(sortBoxList)
    print(f"{test} {max(sortBoxList)-min(sortBoxList)}")

        
        

        
    
        
        
        
