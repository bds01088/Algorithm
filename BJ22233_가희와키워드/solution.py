'''
메모장에 존재하는 키워드가 주어지고
글을 쓸때 사용한 키워드가 메모장 목록에서 사라진다
글을 쓰고 난 후 메모장에 남은 키워드 개수를 출력하자
입력
5 2
map
set
dijkstra
floyd
os
map,dijkstra
map,floyd

출력
3
2
'''
import sys

n, m = map(int, sys.stdin.readline().split())

memolist = {}
visit = [0 for _ in range(n)]
for i in range(n):
    memolist[sys.stdin.readline().rstrip()] = 1

ans = n
for i in range(m):
    used = []
    used.extend(sys.stdin.readline().rstrip().split(','))
    for ele in used :
        #딕셔너리에서 []로 찾으면 키값이 없을때 에러뜸
        #get으로하면 키값이 없을때 none을 반환
        if memolist.get(ele) == 1 :
            memolist[ele] = 0
            ans -= 1
    print(ans)











'''
#시간초과뜸
from collections import deque

n, m = map(int, input().split())

memolist = deque()
for i in range(n):
    memolist.append(input())

for i in range(m):
    used = []
    used.extend(input().split(','))
    for ele in used:
        if ele in memolist:
            memolist.pop(memolist.index(ele))
    print(len(memolist))
    '''