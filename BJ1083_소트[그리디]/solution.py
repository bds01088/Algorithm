N = int(input())

arr = list(map(int, input().split()))

S = int(input())

sarr = sorted(arr, reverse=True)

for i in range(N-1):
    idx = i
    #초기값 설정이 잘못됐다
    mmax = arr[i]
    for j in range(i+1, N):
        if j-i > S:
            break
        #비교대상이 잘못됐다
        if mmax < arr[j] :
            if j-i <= S :
                idx = j
                mmax = arr[j]
    
    S -= idx-i
    
    arr.insert(i, arr.pop(idx))
    
    if S <= 0 :
        break
    if arr == sarr :
        break

for e in arr:
    print(e, end=' ')