import copy
n = int(input())

for i in range(n) :
    amount = int(input())
    pigs = list(map(int, input().split()))
    ans = 1
    while sum(pigs) <= amount :
        arr = [0,0,0,0,0,0]
        for j in range(6):
            if j < 3:
                arr[j] = pigs[j] + pigs[j-1] + pigs[j+1] + pigs[j+3]
            else :
                if j == 5 :
                    arr[j] = pigs[j] + pigs[j-1] + pigs[0] + pigs[j-3]
                else :
                    arr[j] = pigs[j] + pigs[j-1] + pigs[j+1] + pigs[j-3]
        pigs = copy.deepcopy(arr)
        ans += 1
    print(ans)