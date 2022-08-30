n = int(input())

problems = list(input())

ans = 1
if problems[0] == 'R' :
    i = 1
    while i < len(problems) :
        if problems[i] != problems[0] :
            ans += 1
            while i < len(problems) and problems[i] != problems[0] :
                i += 1
        else :
            i += 1
else :
    i = 1
    while i < len(problems) :
        if problems[i] != problems[0] :
            ans += 1
            while i < len(problems) and problems[i] != problems[0] :
                i += 1
        else :
            i += 1
print(ans)