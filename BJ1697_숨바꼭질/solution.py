from collections import deque

def BFS(num, cnt):
    global m, visit
    q = deque()
    q.append([num,cnt])
    visit[num] = 1

    while q :
        now = q.popleft()
        if now[0] == m :
            return now[1]
        if visit.get(now[0]*2) == None and 0 <= now[0]*2 <= 100000:
            visit[now[0]*2] = 1
            now_num = now[0]*2
            now_cnt = now[1]+1
            q.append([now_num, now_cnt])
        if visit.get(now[0]+1) == None and 0 <= now[0]+1 <= 100000:
            visit[now[0]+1] = 1
            now_num = now[0]+1
            now_cnt = now[1]+1
            q.append([now_num, now_cnt])
        if visit.get(now[0]-1) == None and 0 <= now[0]-1 <= 100000:
            visit[now[0]-1] = 1
            now_num = now[0]-1
            now_cnt = now[1]+1
            q.append([now_num, now_cnt])


n, m = map(int, input().split())

ans = 999999999
cnt = 0
visit = {}
ans = BFS(n, cnt)
print(ans)

'''
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k :
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x]+1
                q.append(nx)
MAX = 10 **5
dist = [0] * (MAX+1)
n, k = map(int, input().split())

bfs()
'''