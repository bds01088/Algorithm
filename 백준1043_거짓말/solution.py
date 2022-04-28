'''
과장된 얘기를 할 수 있는 파티의 수를 구하자
사람의 수 n과 파티의 수 m 이 주어지고
진실을 아는 사람의 수 p와 각 사람의 번호q가 p개만큼 주어진다 한줄에
파티에 참여하는 수와 참여하는 사람의 번호가 주어진다

진실을 아는 사람과 같은 파티를 참여하는 사람들은 모두 진실을 알게된다
즉
진실을 아는 사람 목록을 만들고
그사람들과 파티에 참석한 사람들과 노드 연결을 하자
모두 다 받아놓고
각 파티의 status를 0으로 할지 1로 할지 해서 최종 sum을 구하면 될듯?

'''
from collections import deque

n, m = map(int, input().split())

know_num, *know_list = map(int, input().split())

arr = [0 for _ in range(n+1)]
for i in know_list :
    arr[i] = 1

board = [[0]*(n+1) for _ in range(n+1)]
party = []
for i in range(m):
    party_pnum, *party_plist = map(int, input().split())
    for p in range(party_pnum):
        for q in range(p, party_pnum):
            board[party_plist[p]][party_plist[q]] = 1
            board[party_plist[q]][party_plist[p]] = 1
    party.append(party_plist)

for i in know_list:
    deq = deque()
    deq.append(i)
    while deq :
        now = deq.pop()
        for l in range(n+1):
            if board[now][l] == 1 and arr[l] == 0 :
                deq.append(l)
                arr[l] = 1

ans = 0

for ppp in party:
    flag = 0
    for i in ppp :
        if arr[i] == 1:
            flag = 1
            break
    if flag == 0:
        ans += 1

print(ans)



