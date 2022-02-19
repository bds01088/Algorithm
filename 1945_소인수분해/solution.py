'''
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.
'''
import sys
sys.stdin = open("input.txt")

tc = int(input())
for t in range(tc):
    n = int(input())
    a, b, c, d, e = 0,0,0,0,0
    while n%2 == 0 :
        a += 1
        n = n//2
    while n%3 == 0 :
        b += 1
        n = n//3
    while n%5 == 0 :
        c += 1
        n = n//5
    while n%7 == 0 :
        d += 1
        n = n//7
    while n%11 == 0 :
        e += 1
        n = n//11
    if n == 1 :
        print(f'#{t+1} {a} {b} {c} {d} {e}')
