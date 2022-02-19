'''
주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.
'''

import sys
sys.stdin = open("input.txt")


for _ in range(10):
    t = int(input())
    c = input()
    s = input()
    cnt = 0
    for i, char in enumerate(s) :
        if char == c[0] :
            if s[i:i+len(c)] == c :
                cnt += 1
    print(f'#{t} {cnt}')