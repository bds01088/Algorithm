'''
0~1 사이의 10진수 n을 2진수로 바꾸려고한다
소수점 아래 12자리 이내인 이진수로 표현할 수 있으면
0.을 제외한 나머지 숫자 출력
13자리 이상일 경우 overflow출력

소수점을 2진수로 바꾸는 법
*2를해서 정수부분을 값으로 가져오면 된다
0.625일 경우
0.625*2 = 1.25 이므로 1
0.25*2 = 0.5 이므로 0
0.5*2 = 1.0 이므로 1
1.0이 나오면 계산 종료
'''

import sys
import math
sys.stdin = open('input.txt')

tc = int(input())

for t in range(tc):
    n = float(input())
    result = ''
    while len(result) < 13 :
        if n*2 > 1.0 :
            result += '1'
            n = n*2-1
        elif n*2 < 1.0 :
            result += '0'
            n = n*2
        elif math.isclose(n*2, 1.0) :
            result += '1'
            break
    if len(result) < 13 :
        print(f'#{t+1} {result}')
    else :
        print(f'#{t + 1} overflow')
