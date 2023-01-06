from collections import defaultdict, deque

def BFS(start):
    global visit, plan
    visit.append(start)
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()

        for node in board[now] :
            if node not in visit :
                visit.append(node)
                q.append(node)
    
    if set(plan).intersection(set(visit)) == set(plan) :
        return True
    else :
        return False

    

N = int(input())
M = int(input())
board = defaultdict(list)
visit = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1 :
            board[i].append(j)
plan = list(map(lambda x : int(x)-1, input().split()))

result = BFS(plan[0])

if result :
    print("YES")
else :
    print("NO")