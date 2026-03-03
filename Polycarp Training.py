n = int(input())
a = list(map(int, input().split()))
a.sort()
day = 1
for problems in a:
    if problems >= day:
        day += 1
print(day - 1)
