'''
올바르게 완성된 스도쿠일 경우 1
아닐 경우 0
'''
import sys
sys.stdin = open("input.txt")

tc = int(input())
for t in range(tc):
    sdq = []
    for _ in range(9) :
        sdq.append(list(map(int, input().split())))
    plag = 0

    for i in range(9):
        # 가로 검증
        prove = [0]*9
        for j in range(9) :
            prove[sdq[i][j]-1] = 1
        if sum(prove) != 9 :
            plag += 1
        #세로 검증
        prove = [0]*9
        for j in range(9) :
            prove[sdq[j][i]-1] = 1
        if sum(prove) != 9 :
            plag += 1
        #사각형 검증
        for j in range(9):
            if i in [0, 3, 6] and j in [0, 3, 6]:
                prove = [0]*9
                for p in range(i,i+3):
                    for q in range(j, j+3) :
                        prove[sdq[p][q]-1] = 1
                if sum(prove) != 9:
                    plag += 1
    if plag != 0 :
        print(f'#{t+1} 0')
    else :
        print(f'#{t + 1} 1')