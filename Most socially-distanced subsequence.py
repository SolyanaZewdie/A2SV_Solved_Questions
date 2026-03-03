t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    if n == 2:
        print(2)
        print(p[0], p[1])
        continue
    ans = [p[0]]
    for i in range(1, n-1):
        if (p[i-1] < p[i] > p[i+1]) or (p[i-1] > p[i] < p[i+1]):
            ans.append(p[i])
    ans.append(p[-1])
    print(len(ans))
    print(*ans)
