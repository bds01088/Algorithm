'''
16진수의 숫자 개수가 주어지고
16진수 숫자들이 주어진다
이를 4자리의 2진수로 표현하여 나타내라
4자리가 안되는 2진수는 앞자리를 0으로 채워서 출력
'''

import sys
sys.stdin = open('input.txt')

tc = int(input())

for t in range(tc):
    n, num_16 = input().split()
    n = int(n)
    result = ''
    for i in range(n):
        temp = str(int(num_16[i], base=16))
        temp = bin(int(temp)).replace('0b', '')
        #print(temp)
        while len(temp) < 4 :
            temp = '0'+temp
        #print(temp)
        result += temp
    print(f'#{t+1} {result}')