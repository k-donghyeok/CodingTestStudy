col,count=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))


# sum=0


# for i in sorted(a,reverse=True)[:col-count]:
#     sum+=i
# for i in sorted(b,reverse=True)[:count]:
#     sum+=i
# print(sum)


a=sorted(a)
b=sorted(b,reverse=True)

for i in range(count):
    if(a[i]<b[i]):
        a[i],b[i]=b[i],a[i]
    
print(sum(a))