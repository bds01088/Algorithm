from itertools import combinations
from collections import defaultdict, deque

def BFS(guList):
    guList = list(guList)
    visit = [False for _ in range(len(guList))]
    start = guList[0]
    visit[guList.index(start)] = True

    q = deque()
    q.append(start)
    tmp = [start]

    while q :
        now = q.popleft()

        for next in board[now] :
            if next in guList :
                idx = guList.index(next)
                if visit[idx] == False :
                    visit[idx] = True
                    q.append(next)
                    tmp.append(next)
    
    if set(tmp) == set(guList) :
        return True
    else :
        return False
            


N = int(input())

pop = list(map(int, input().split()))

board = defaultdict(list)

for i in range(N):
    lineList = list(map(int, input().split()))
    for j in range(1, lineList[0]+1):
        board[i].append(lineList[j]-1)

totalSet = set(range(N))

spop = sum(pop)
mmin = 9999999
for i in range(1, N//2+1) :
    #한쪽 구를 구하면, 나머지 하나의 구는 자동 확정이니까
    #1개하면 반대 구는 5개 ~~ -> 3개면 반대 구 3개로 모든 경우의 수를 확인함
    candiList = list(combinations(range(N), i))
    #경우의 수 중에서 두개의 구 인구수 차이가 이미 구해져있는 값보다 클 경우 스킵하기
    for candi in candiList :
        anotherCandi = totalSet.difference(set(candi))

        #차이값이 갱신안되는 조건이면 스킵하기
        a = 0
        for num in candi:
            a += pop[num]
        diff = abs((spop-a)-a)
        if mmin <= diff :
            continue
        
        if BFS(candi) and BFS(anotherCandi) :
            mmin = diff

if mmin == 9999999 :
    print(-1)
else :
    print(mmin)
        
        