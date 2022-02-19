'''
정수 10개를 받아 부분집합이 0이 되는 것이 존재하는지 알아보자

'''

import sys
sys.stdin = open("practice2_input.txt")

tc = int(input())

for t in range(tc):
    arr = list(map(int, input().split()))
    n = len(arr)
    result = 0
    for i in range(1<<n) :
        psum = []
        for j in range(n) :
            if i & (1<<j) :
                psum.append(arr[j])
        if sum(psum) == 0 and len(psum) != 0:
            result = 1
            break
    print(f'#{t+1} {result}')