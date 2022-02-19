'''
시작 1 끝 n인 책에서 찾는 쪽번호가
중간 페이지 int((1+n)/2)와 같아질 때 탐색한 횟수가
적은 쪽의 이름이 나오게 함
동률일시 0을 출력
'''

import sys
sys.stdin = open("input.txt")

def page_find(e, n, s = 1) :
    cnt = 0
    #찾을때까지 무한반복
    while True :
        if (s+e)//2 != n :
            cnt += 1
            if (s+e)//2 < n :
                s = (s+e)//2
            else :
                e = (s+e)//2
        else :
            return cnt

tc = int(input())
for t in range(tc):
    e, a, b = map(int, input().split())
    s = 1
    #두개의 결과값을 따로 구해서 비교하기
    result_a = page_find(e, a)
    result_b = page_find(e, b)
    if result_b == result_a :
        print(f'#{t+1} 0')
    elif result_a < result_b :
        print(f'#{t+1} A')
    else :
        print(f'#{t+1} B')
