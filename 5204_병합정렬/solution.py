'''
병합정렬을 실행하고자 한다
n개의 정렬대상을 가진 리스트l을 분할할 때
l[0:n//2], l[n//2:n]으로 분할한다
병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다

2 2 1 1 3 -> 2 0
1 1 2 2 3 으로 정렬될때
첫번째 출력값은 n//2위치의 값이고
2 2          1 1 3
2   2        1 1    3
             1   1
병합정렬이 이렇게 진행될텐데
병합 당시 좌측이 우측보다 클때가 없다

7 5 4 1 2 10 3 6 9 8이면?
7 5 4 1 2          10 3 6 9 8
7 5 4       1 2        10 3 6     9 8
7 5     4   1   2      10 3   6   9   8
7   5                  10   3
7 5 합병시 +1
10 3 합병시 +1
5 7   4 합병시 +1
1 2 합병시 없음
3 10  6 합병시 +1
9 8 합병시 +1
4 5 7    1 2 합병시 없음
3 6 10   8 9 합병시 +1
1 2 4 5 7    3 6 8 9 10 합병시 없음
'''

import sys
sys.stdin = open('input.txt')

def mergesort(arr):
    global cnt
    if len(arr) == 1 :
        return arr
    else :
        left = arr[0:len(arr)//2]
        right = arr[len(arr)//2:len(arr)]
        s_left = mergesort(left)
        s_right = mergesort(right)
        if s_left[-1] > s_right[-1] :
            cnt += 1
        m_arr = []
        i = 0
        j = 0
        while len(s_left) != i and len(s_right) != j :
            if s_left[i] <= s_right[j] :
                m_arr.append(s_left[i])
                i += 1
            elif s_left[i] > s_right[j] :
                m_arr.append(s_right[j])
                j += 1
        if len(s_left) != i and len(s_right) == j :
            m_arr += s_left[i:len(s_left)]
        elif len(s_left) == i and len(s_right) != j:
            m_arr += s_right[j:len(s_right)]
    return m_arr


tc = int(input())

for t in range(tc):
    n = int(input())
    arr = list(map(int ,input().split()))
    cnt = 0
    new_arr = mergesort(arr)
    print(f'#{t+1} {new_arr[n//2]} {cnt}')