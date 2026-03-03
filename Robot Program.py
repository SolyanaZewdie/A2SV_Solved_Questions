t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()
    if x == 0:
        print(k // n)
        continue
    pos = x
    ans = 0
    for i in range(min(n, k)):
        if s[i] == 'L':
            pos -= 1
        else:
            pos += 1
        if pos == 0:
            ans += 1
            break
    if ans == 0:
        print(0)
        continue
    ans += (k - i - 1) // n
    print(ans)
