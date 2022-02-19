'''
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10  1  9  2  8  3  7  4  6  5
-1  0 -2  1 -3  2 -4  3 -5  4
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
11  1  10  2  9  3  8  4  7  5  6
-1  0  -2  1 -3  2 -4  3 -5  4 -6
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

해결방법
일단은 정렬하고
새 리스트에 맨처음 맨끝을 번갈아가면서 넣어주면 되지않을까?
추출한다음 기존 리스트에서 삭제시켜주거나 인덱스 조절하고
'''

import sys
sys.stdin = open("input.txt")

def BubbleSort(a, n) :
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
    return a

tc = int(input())
for t in range(tc):
    l = int(input())
    arr = list(map(int, input().split()))
    #먼저 정렬하고
    arr = BubbleSort(arr, l)
    #새로운 리스트 만들기
    sarr = [0]*l
    p = 0
    q = -1
    for i in range(l):
        #홀수일때는 작은 수
        if i%2 == 1:
            sarr[i] = arr[p]
            #앞에서 불러오기 때문
            p+=1
        #짝수일때는 큰 수
        else :
            sarr[i] = arr[q]
            #뒤에서 불러오기 때문
            q-=1
    print(f'#{t+1}', end=' ')
    #문제에서 10개만 출력하라했음
    for n in range(10) :
        print(sarr[n], end=' ')
    print()


