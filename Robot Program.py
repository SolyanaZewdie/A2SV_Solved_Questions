t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pref = [0] * n
    cur = 0
    for i in range(n):
        if s[i] == 'L':
            cur -= 1
        else:
            cur += 1
        pref[i] = cur
    
    first_hit = -1
    for i in range(n):
        if x + pref[i] == 0:
            first_hit = i + 1
            break
    
    if first_hit == -1 or first_hit > k:
        print(0)
        continue
    
    ans = 1
    remaining = k - first_hit
    
    cycle_hit = -1
    for i in range(n):
        if pref[i] == 0:
            cycle_hit = i + 1
            break
    
    if cycle_hit == -1:
        print(ans)
    else:
        ans += remaining // cycle_hit
        print(ans)
