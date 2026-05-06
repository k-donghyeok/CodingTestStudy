

T = int(input())

for test_case in range(1,T+1):
    N,M = map(int,input().split())

    array=[]
    temp=[]
    for i in range(N):
        array.append(list(input()))

    xindex=0
    yindex=0
    print(array)
    for i in range(len(array)):
        for j in range(len(array[i])):
            if(array[i][j]=='1'):
                xindex=j
                yindex=i
    

    code=[]
    count=0
    scanner={
        '0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9
    }

    
    encryptedCode=array[yindex][xindex-55:xindex+1]
    encryptedCode=''.join(map(str,encryptedCode))
    for i in range(0,56,7):
        temp=encryptedCode[i:i+7]
        code.append(scanner[temp])
    
    total=0
    for i in code:
        total+=i
    sum= 3*(code[0]+code[2]+code[4]+code[6])+(code[1]+code[3]+code[5]+code[7])
    if(sum%10 ==0):
        print(f"#{test_case} {total}")
        