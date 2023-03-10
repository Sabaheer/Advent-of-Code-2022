import re

pattern = re.compile(r"-?\d+")

Y = 2000000

known = set()

intervals = []

for line in open("Input15.txt"):
    sx, sy, bx, by = map(int, pattern.findall(line))
    
    d = abs(sx - bx) + abs(sy - by)
    o = d - abs(sy - Y)

    if o < 0:
        continue

    lx = sx - o
    hx = sx + o
    
    intervals.append((lx, hx))
    
    if by == Y:
        known.add(bx)

intervals.sort()

q = []

for lo, hi in intervals:
    if not q:
        q.append([lo, hi])
        continue

    qlo, qhi = q[-1]

    if lo > qhi + 1:
        q.append([lo, hi])
        continue
    
    q[-1][1] = max(qhi, hi)

cannot = set()

for lo, hi in q:
    for x in range(lo, hi + 1):
        cannot.add(x)

print(len(cannot - known))

# -----------------------------------------------------------------
# Question 
# Part 2

import re

pattern = re.compile(r"-?\d+")

lines = [list(map(int, pattern.findall(line))) for line in open("Input15.txt")]

M = 4000000

for Y in range(M + 1):
    intervals = []

    for sx, sy, bx, by in lines:
        d = abs(sx - bx) + abs(sy - by)
        o = d - abs(sy - Y)

        if o < 0:
            continue

        lx = sx - o
        hx = sx + o
        
        intervals.append((lx, hx))

    intervals.sort()

    q = []

    for lo, hi in intervals:
        if not q:
            q.append([lo, hi])
            continue

        qlo, qhi = q[-1]

        if lo > qhi + 1:
            q.append([lo, hi])
            continue
        
        q[-1][1] = max(qhi, hi)
    
    x = 0
    for lo, hi in q:
        if x < lo:
            print(x * 4000000 + Y)
            exit(0)
        x = max(x, hi + 1)
        if x > M:
            break