'''
import sys
input = sys.stdin.readline
input().strip().split()
훨빠름
'''
n, m = map(int, input().split())

pkm = {}

for i in range(1, n+1):
    pkm[input()] = i

reverse_pkm = dict(map(reversed, pkm.items()))

for i in range(m):
    x = input()
    if x.isdigit() :
        x = int(x)
        print(reverse_pkm.get(x))
    else :
        print(pkm.get(x))

