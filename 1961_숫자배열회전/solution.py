'''
90도 회전
1	(0, 0)	(0, 2)
2	(0, 1)	(1, 2)
3	(0, 2)	(2, 2)
회전 전의 열 번호와 회전 후의 행 번호가 일치한다.
그리고 회전 후의 열은 N-1 에서 회전 전의 행을 뺀 값과 같다.

180도 회전
1	(0, 0)	(2, 2)
2	(0, 1)	(2, 1)
3	(0, 2)	(2, 0)
회전 후의 행 번호는 N-1 의 값에서 전의 행 번호를 뺀 것과 같다.
회전 후의 열 번호는 N-1 의 값에서 전의 열 번호를 뺀 것과 같다.

270도 회전
1	(0, 0)	(2, 0)
2	(0, 1)	(1, 0)
3	(0, 2)	(0, 0)
회전 후의 열과 전의 행이 일치한다.
후의 행 번호는 N-1 에서 전의 열 번호를 뺀 값과 일치한다.
'''

import sys
sys.stdin = open("input.txt")

tc = int(input())
for t in range(tc):
    n = int(input())
    arr = []
    arr90 = []
    arr180 = []
    arr270 = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
        arr90.append([0]*n)
        arr180.append([0] * n)
        arr270.append([0] * n)


    for i in range(n):
        for j in range(n):
            #회전 전의 열 번호와 회전 후의 행 번호가 일치한다.
            #그리고 회전 후의 열은 N-1 에서 회전 전의 행을 뺀 값과 같다.
            arr90[i][j] = arr[j][n-1-i]
            #회전 후의 행 번호는 N-1 의 값에서 전의 행 번호를 뺀 것과 같다.
            #회전 후의 열 번호는 N-1 의 값에서 전의 열 번호를 뺀 것과 같다.
            arr180[i][j] = arr[n-1-i][n-1-j] #arr90[j][n-1-i]
            #회전 후의 열과 전의 행이 일치한다.
            #후의 행 번호는 N-1 에서 전의 열 번호를 뺀 값과 일치한다.
            arr270[i][j] = arr[n-1-j][i]
    print(f'#{t+1}')
    for a1, a2, a3 in zip(arr90, arr180, arr270):
        print(f'{"".join(map(str,a1))} {"".join(map(str,a2))} {"".join(map(str,a3))}')
