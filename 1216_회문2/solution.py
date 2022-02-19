'''
회문중에 가장 긴 회문의 길이를 구하라
A, B, C로만 이루어진 100x100배열
max_len을 1으로 주고
회문의 길이를 max_len보다 긴 것만 찾고

'''

import sys
sys.stdin = open("input.txt")

def isP(p) :
    if p == p[::-1] :
        return 1
    else :
        return 0

for _ in range(10) :
    t = int(input())
    board = [list(input()) for _ in range(100)]
    another_board = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            another_board[j][i] = board[i][j]
    max_len = 2
    for i in range(100) :
        for j in range(100):
            #j에서부터 끝까지를 맨처음으로 잡아야함
            target_len = 100-j
            #현재 최대길이가 타겟길이보다 작을 경우에 찾음
            while target_len > max_len or target_len > 1:
                temp = []
                another_temp = []
                #회문판별할 문자열 추출하기
                for p in range(j, j+target_len) :
                    temp.append(board[i][p])
                    another_temp.append((another_board[i][p]))
                #회문이면 최대길이와 비교하여 크다면 대입해줌
                if isP(temp) == 1 :
                    if max_len < len(temp):
                        max_len = len(temp)
                elif isP(another_temp) == 1 :
                    if max_len < len(another_temp) :
                        max_len = len(another_temp)
                #한바퀴 돌고 나면 길이를 줄여줌
                #타겟길이가 최대길이보다 작은건 while문에서 판단해줄거임
                target_len -= 1
    print(f'#{t} {max_len}')




'''
#1 18
#2 17
#3 17
#4 20
#5 18
#6 21
#7 18
#8 18
#9 17
#10 18
'''