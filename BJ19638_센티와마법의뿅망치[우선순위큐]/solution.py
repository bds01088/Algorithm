import heapq

n, centi, hammer = map(int, input().split())

heap = []

for i in range(n):
    a = int(input())
    heapq.heappush(heap, [-a, a])


newhammer = hammer
while hammer > 0 :
    x = heapq.heappop(heap)
    if x[1] >= centi :
        nx = max(1, x[1]//2)
        x = [-nx, nx]
        hammer -= 1
        heapq.heappush(heap, x)
    elif x[1] < centi :
        heapq.heappush(heap, x)
        break

t = heapq.heappop(heap)[1]

if t < centi :
    print("YES")
    print(newhammer-hammer)
else:
    print("NO")
    print(t)

