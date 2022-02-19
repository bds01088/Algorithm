'''
최초 인덱스 1로 부여
내 최소값이 타 최대값과 비교했을때 크면 최소인덱스+1
내 최대값이 타 최소값과 비교했을때 크거나 같을 경우 최대인덱스에서 +1
'''
import sys
sys.stdin = open("input.txt")
n = int(input())
min_list = []
max_list = []
min_idx_list = []
max_idx_list = []
for i in range(n):
    std, err = map(int, input().split())
    min_list.append(std-err)
    max_list.append(std+err)
    min_idx_list.append(1)
    max_idx_list.append(1)

for i in range(n):
    for j in range(n):
        if i != j :
            if min_list[i] > max_list[j] :
                min_idx_list[i] += 1
            if max_list[i] >= min_list[j] :
                max_idx_list[i] += 1

for i in range(n):
    print(min_idx_list[i], max_idx_list[i])
