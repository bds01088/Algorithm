'''
문제
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 값 구하기

입력
첫 줄에 테스트케이스 갯수(1 <= t <= 50)가 주어지고
케이스별 들어올 데이터 갯수(5 <= n <= 1000)가 주어지고
양수의 정수가 들어온다 (1 <= a <= 1000000)

출력
#테스트케이스번호 결과값

해결방법
for문을 돌면서 min 변수와 max 변수를 찾아내고
for문이 끝난뒤 max-min 으로 출력하면 끝
'''

import sys
sys.stdin = open('input.txt')

tc = int(input())

def mmm(n, case):
    max = 0
    min = 10000000
    for num in case :
        if num > max :
            max = num
        if num < min :
            min = num
    result = max - min
    return result

for i in range(tc):
    n = int(input())
    case = list(map(int, input().split()))
    r = mmm(n, case)
    print(f'#{i+1} {r}')
