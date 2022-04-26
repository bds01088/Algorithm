'''
n, m이 주어지고
n부터 m까지의 수를
영어로 표현한 뒤
영어 알파벳 순서대로 정렬하자
10이면
one zero
21
two one
이렇게
아스키코드로 변환해서 비교하면 될듯
'''

n, m = map(int,input().split())
num_char = ['zero', 'one', 'two', 'three', 'four', 'five', 'six','seven','eight','nine']
arr = [i for i in range(n, m+1)]

num_list = []

for i in arr:
    temp = []
    for j in str(i):
        for k in num_char[int(j)]:
            temp.append(ord(k))
    temp.append(i)
    num_list.append(temp)

# print(num_list)
# print(sorted(num_list))

ans = sorted(num_list)
aaa = 0
for i in range(m-n+1):
    aaa += 1
    print(ans[i][-1], end=' ')
    if aaa == 10 :
        aaa = 0
        print()
# num_list.sort(key= lambda x : )


