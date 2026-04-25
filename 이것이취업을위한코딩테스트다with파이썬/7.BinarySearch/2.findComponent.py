import sys

n=int(input())
store=[x for x in map(int,sys.stdin.readline().split())]
m=int(input())
customer=[x for x in map(int,sys.stdin.readline().split())]

#완전탐색
def findComponent(store,customer):
    for i in customer:
        for j in store:
            if(i==j):
                print("Yes",end=' ')
                break
        if(j==store[-1]):
            print("No",end=' ')    
                

#findComponent(store,customer)

#이진탐색
def findComponent2(start,end,target):
    if(start>end):
        return 'No'
    middle=(start+end)//2
    if(store[middle]>target):
        return findComponent2(start,middle-1,target)
    elif(store[middle]<target):
        return findComponent2(middle+1,end,target)
    else:
        return 'Yes'

#store.sort()
#for i in customer:
#    print(findComponent2(0,len(store)-1,i),end=' ')

#계수정렬
def findComponent3(store,customer):
    visited=[0 for _ in range(1000001)]

    for i in store:
        visited[i]+=1

    for i in customer:
        if(visited[i]==1):
            print('Yes',end=' ')
        else:
            print('No',end=' ')

#findComponent3(store,customer)
#set 이용
def findComponent4(store,customer):

    store=set(store)

    for i in customer:
        if i in store:
            print('Yes',end=' ')
        else:
            print('No',end=' ')

findComponent4(customer)
