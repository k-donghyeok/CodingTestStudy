#2:10
#2:43
# 입력받은 배열에서 뒤에서부터 1을 찾아서 찾으면 거기서부터 56개 슬라이싱
# 슬라이싱한 배열을 7개씩 잘라서 해당하는 코드가있는지 확인
# 잇으면 해당하는 숫자로변경 후 맞는 암호코드인지 검사 맞으면 합을 출력 아니면 0출력

T=int(input())

for test_Case in range(1,1+T):

    n,m =map(int,input().split())

    array=[]
    for y in range(n):
        array.append(input().rstrip())
    #print(array)
    temp=''
    stop=False
    for y in range(n):
        for x in range(m-1,-1,-1):
            if(array[y][x]=='1'):
                #print(x,y)
                temp=array[y][x-55:x+1]
                #print(temp)
                stop=True
                break
        if(stop):
            break
    codes=[
        '0001101', #0
        '0011001', #1
        '0010011', #2
        '0111101', #3
        '0100011', #4
        '0110001', #5
        '0101111', #6
        '0111011', #7
        '0110111', #8
        '0001011' #9
    ]
    result=[]
    #print(temp)
    for i in range(0,56,7):
        #print(temp[i:i+7])
        if(temp[i:i+7] in codes):
            for j in range(len(codes)):
                if(temp[i:i+7]==codes[j]):
                    result.append(j)
    hol=0
    jjak=0
    for i in range(1,len(result)+1):
        if(i%2==1):
            hol+=result[i-1]
        else:
            jjak+=result[i-1]
   # print(result,hol,jjak,((hol*3) + jjak ))
    if(((hol*3) + jjak )%10==0):
        print(f'#{test_Case} {hol+jjak}')
    else:
        print(f'#{test_Case} 0')
