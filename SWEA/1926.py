num=int(input())

for i in range(1,num+1):
    stri=str(i)
    if('3' in stri or '6' in stri or '9' in stri):
        for j in stri:
             if(j=='3' or j=='6' or j=='9'):
                print('-',end='')
        print('',end=' ')
    else:
        print(stri,end=' ')
        