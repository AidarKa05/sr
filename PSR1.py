import sys
n = int(input())
lines = []
k = 0
f = True
for el in sys.stdin:
    el = el.replace('\n', '')
    if f:
        lines.append([el])
        f = False
    else:
        lines[k].append(el)
        f = True
        k += 1
print(lines)
for i in range(k):
    allow, ln = lines[i][0], lines[i][1]
    count = []
    fn = []
    c = 0
    for j in range(len(ln)):
        if ln[j] in allow and len(fn) == 0:
            fn.append(j)
            c = 0
        if ln[j] in allow and len(fn) > 0:
            if j - fn[c] <= n:
                fn.append(j)
                c += 1
            else:
                count.append(ln[fn[0]:(fn[-1]+1)])
                c = 0
                fn = [j]
    print(count)


