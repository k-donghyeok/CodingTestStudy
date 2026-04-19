targetHour = int(input())
number=3
result=0
for currentHour in range(targetHour+1):
    for currentMinute in range(60):
        for currnetSecond in range(60):
            currentTime=str(currentHour)+str(currentMinute)+str(currnetSecond)
            if(str(number) in currentTime):
                result+=1
print(result)