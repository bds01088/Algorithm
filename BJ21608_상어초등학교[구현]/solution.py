import sys

input = sys.stdin.readline

'''
상하좌우만 인접칸으로 인식

1. 비어있는 칸 중에서 좋아하는 학생이 가장 많이 인접한 칸으로 정한다
2. 1을 만족한 칸이 여러개면, 비어있는 칸이 가장 많이 인접한 곳으로 정한다
3. 2를 만족한 칸이 여러개면, 행의 번호가 가장 작은 칸 우선으로, 그다음 열이 가장 작은 칸으로

만족도는 1=1, 2=10, 3=100, 4=1000
배치가 다 끝나고 만족도를 구한다
'''

def Solution(student):
    #좋아하는 학생이 있는지 먼저 파악하자
    candi_loc = [[[0,0] for _ in range(n)] for _ in range(n)]
    isLikeFriend = False
    for i in range(n):
        for j in range(n):
            if loc[i][j] == 0 :
                for d in range(4):
                    if 0 <= (i+dr[d]) < n and 0 <= (j+dc[d]) < n :
                        if loc[i+dr[d]][j+dc[d]] in student[1:] :
                            candi_loc[i][j][0] += 1
                            isLikeFriend = True
                        if loc[i+dr[d]][j+dc[d]] == 0 :
                            candi_loc[i][j][1] += 1

    #가장 친한친구가 많은 위치 찾기
    maxBlank = 0
    maxFriend = 0
    maxR = 9999
    maxC = 9999
    for i in range(n):
        for j in range(n):
            if loc[i][j] == 0:
            #좋아하는 친구가 있다면?
                if isLikeFriend == True :
                    #자리 중에 호감도가 제일 높은 위치찾기
                    if maxFriend < candi_loc[i][j][0] :
                        maxFriend = candi_loc[i][j][0]
                        maxBlank = candi_loc[i][j][1]
                        maxR = i
                        maxC = j
                    #호감도가 똑같다면
                    elif maxFriend == candi_loc[i][j][0] :
                        #빈칸이 가장 많은거 우선
                        if maxBlank < candi_loc[i][j][1]:
                            maxFriend = candi_loc[i][j][0]
                            maxBlank = candi_loc[i][j][1]
                            maxR = i
                            maxC = j
                        elif maxBlank == candi_loc[i][j][1] :
                            #row가 가장 작은거로 변경
                            if maxR > i :
                                maxFriend = candi_loc[i][j][0]
                                maxBlank = candi_loc[i][j][1]
                                maxR = i
                                maxC = j
                            #row도 같다면
                            elif maxR == i :
                                #col이 가장 작은거로
                                if maxC > j :
                                    maxFriend = candi_loc[i][j][0]
                                    maxBlank = candi_loc[i][j][1]
                                    maxR = i
                                    maxC = j
                else :
                    #자리 중에 빈칸이 가장 많이 연결된 자리 찾기
                    if maxBlank < candi_loc[i][j][1] :
                        maxBlank = candi_loc[i][j][1]
                        maxR = i
                        maxC = j
                    #호감도가 똑같다면
                    elif maxBlank == candi_loc[i][j][1] :
                        #row가 가장 작은거로 변경
                        if maxR > i :
                            maxBlank = candi_loc[i][j][1]
                            maxR = i
                            maxC = j
                        #row도 같다면
                        elif maxR == i :
                            #col이 가장 작은거로
                            if maxC > j :
                                maxBlank = candi_loc[i][j][1]
                                maxR = i
                                maxC = j
    return [maxR, maxC]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n = int(input().strip())

loc = [[0 for _ in range(n)] for _ in range(n)]

students = []
for i in range(n*n):
    students.append(list(map(int,input().strip().split())))
    if students[i][0] == 3 :
        xx=0
    res = Solution(students[i])
    loc[res[0]][res[1]] = students[i][0]


dic = {}
for i in range(n*n):
    dic[students[i][0]] = students[i][1:]

ans = 0
score = {0 : 0,
         1 : 1,
         2 : 10,
         3 : 100,
         4 : 1000
}

for i in range(n):
    for j in range(n):
        cnt = 0
        for d in range(4):
            if 0 <= (i+dr[d]) < n and 0 <= (j+dc[d]) < n :
                if loc[i+dr[d]][j+dc[d]] in dic[loc[i][j]]:
                    cnt += 1
        ans += score[cnt]
print(ans)
            
