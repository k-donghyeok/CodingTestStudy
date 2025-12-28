#당신은 음식점의 계산을 도와주는 점원 이다 
#카운터에서는 거스름돈으로 사용할 500원 100원 50원 10원 짜리 동전이 무한히 존재한다고 가정한다
#손님에게 거슬러 줘야할 돈이 n 원 일때 거슬러 줘야할 동전의 최소개수를 구하라
#단 거슬러 줘야할 돈 n은 항상 10의 배수이다
import random
i= random.randrange(1,101)
n=10*i
dictCount={}
count=0
print(f"손님이 준돈 : {n} ")

if n>=500:
    dictCount['500원']=n//500
    count+=n//500
    n=n%500
if n>=100:
    dictCount['100원']=n//100
    count+=n//100
    n=n%100
if n>=50:
    dictCount['50원']=n//50
    count+=n//50
    n=n%50
if n>=10:
    dictCount['10원']=n//10
    count+=n//10



print(f"거슬러 줘야할 동전의 최소갯수 : {dictCount} 으로 총{count}개")

    