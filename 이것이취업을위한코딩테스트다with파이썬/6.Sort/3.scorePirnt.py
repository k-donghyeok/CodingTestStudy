headCount=int(input())

studentInfo=[]

for i in range(headCount):
    name,score=input().split()
    score=int(score)
    studentInfo.append((name,score))

   
result=sorted(studentInfo,key= lambda student : student[1])

for i in result:
    print(i[0],end=' ')