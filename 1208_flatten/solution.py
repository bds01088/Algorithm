'''
문제
상자를 옮겨 평탄화를 해야 한다
작업 후 가장 높은 곳과 가장 낮은 곳의 높이 차이가 적게 나야한다
옮길 수 있는 횟수는 제한되어있다
가로 길이는 항상 100이다
모든 위치의 상자높이는 1~100이다
횟수는 1~1000이다
횟수 이내에 평탄화가 이루어진다면 차이값을 반환한다
평탄화 되었을때에는 높이의 차이가 0 또는 1이 나올수밖에없다

입력
테스트케이스 10개가 주어진다
덤프횟수가 주어진다
각 상자의 높이가 주어진다

출력
#테스트케이스넘버 결과값

해결방법
for문으로 덤프횟수만큼 돌면서
상자높이 리스트를 돈다
높이의 최대값과 최소값을 구하고
두개의 차이가 0 또는 1이 되면 차이값을 리턴해준다
아니라면 그 위치에 각각 -1 +1을 해준다
'''

import sys
sys.stdin = open('input.txt')

def flatten(dump, boxes):
    #덤프만큼 for문 돌기
    for i in range(dump) :
        max = 0
        min = 1000
        max_idx = 0
        min_idx = 0
        #최대 최소값과 그 인덱스 찾기
        for idx, h in enumerate(boxes) :
            if max < h :
                max = h
                max_idx = idx
            if min > h :
                min = h
                min_idx = idx
        #만약 차이값이 0이나 1일 경우 바로 리턴
        if (max - min) == 0 or (max - min) == 1 :
            return max-min
        else :
            # 아닐경우 박스 높이 변경
            boxes[max_idx] -= 1
            boxes[min_idx] += 1
    #최종 최대 최소값 찾아서 계산
    max = 0
    min = 1000
    for h in boxes:
        if max < h:
            max = h
        if min > h:
            min = h
    result = max - min
    return result

for t in range(1, 11) :
    dump = int(input())
    box_list = list(map(int, input().split()))
    result = flatten(dump, box_list)
    print(f'#{t} {result}')