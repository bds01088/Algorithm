def solution(arr, l):
    if l >= 2 and arr[-2] > arr[-1] :
        return

    if l == m :
        result.append(arr)
        return
    
    for v in val:
        solution(arr+[v], l+1)
 
n, m = map(int ,input().split())

val = sorted(list(map(int, input().split())))

# print(val)
result = []

solution([], 0)

for i in range(len(result)):
    for j in range(m):
        print(result[i][j], end="")
        print(" ", end="")
    print()
