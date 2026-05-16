# 4:38
# 4:51
# 음 딕셔너리 사용해서 키값을 문자열로 밸류로 숫자를 넣어서 정렬시키면될듯



T=int(input())

for _ in range(1,1+T):
    test_case,n = input().split()

    n=int(n)

    toNum={
          'ZRO': 0,
          'ONE': 1,
          'TWO': 2,
          'THR': 3,
          'FOR': 4,
          'FIV': 5,
          'SIX': 6,
          'SVN': 7,
          'EGT': 8,
          'NIN': 9,
          }
    toStr = {
        0:'ZRO',
        1:'ONE',
        2:'TWO',
        3:'THR',
        4:'FOR',
        5:'FIV',
        6:'SIX',
        7:'SVN',
        8:'EGT',
        9:'NIN',
    }

    array=[toNum.get(x) for x in input().split()]
    #print(array)
    array.sort()
    #print(array)
    array=[toStr.get(x) for x in array]
    print(test_case)
    for i in array:
        print(i,end=' ')
    print()
