'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

import sys
sys.stdin = open("input.txt")

tc= int(input())

for t in range(tc) :
    n, k = map(int, input().split())
    #부분집합을 담을 리스트 생성
    arr = []
    #1부터 12를 원소로 갖는 집합 생성
    l = list(range(1,13))
    for i in range(1<<12) :
        a = []
        #아직까지는 부분집합 구할 때 원리를 잘 모르겠다
        #비트 연산으로 두개가 동시에 1일때만 출력하는거긴한데 조금 헷갈림..
        for j in range(12) :
            if i & (1<<j) :
                a.append(l[j])
        arr.append(a)
    cnt = 0
    for element in arr :
        if len(element) == n and sum(element) == k :
            cnt += 1
    print(f'#{t+1} {cnt}')
