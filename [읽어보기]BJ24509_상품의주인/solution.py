'''
n명의 학생으로 이루어지며
각 학생당 국 영 수 과 점수가 입력으로 들어온다
국 영 수 과 순서대로 1등인 친구가 상품을 받으며
한번 받은 친구는 다른 과목에서 1등 하여도 상품을 받지 않는다
국 영 수 과 순서대로 상품을 받은 학생의 번호를 출력하라
'''

n = int(input())

board = [[0 for _ in range(4)] for _ in range(n+1)]

for i in range(1,n+1):
    arr = list(input().split())
    for j in range(1, 5):
        board[int(arr[0])][j-1] = int(arr[j])

# print(board)

visit = []
for i in range(4):
    m_idx = 0
    m = -1
    for j in range(1, n+1):
        if board[j][i] > m and j not in visit:
            m = board[j][i]
            m_idx = j
    visit.append(m_idx)

for i in visit :
    print(i, end=' ')

'''
따른사람꺼
내가 하고자 했던 방법
n = int(input())
score = []
ans = []
for _ in range(n):
    score.append(list(map(int, input().split())))
score.sort()
for i in range(1, 5):
    temp = max(score, key=lambda x: x[i])
    ans.append(temp[0])
    del score[score.index(temp)]
for i in ans:
    print(i, end=" ")
'''