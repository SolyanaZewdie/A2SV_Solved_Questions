t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    ans = 10**9
    
    for i in range(n - 1):
        if s[i] == 'a' and s[i + 1] == 'a':
            ans = 2
    
    for i in range(n - 2):
        if s[i] == 'a' and s[i + 2] == 'a':
            ans = min(ans, 3)
    
    for i in range(n - 3):
        if s[i:i+4] == "abca" or s[i:i+4] == "acba":
            ans = min(ans, 4)
    
    for i in range(n - 6):
        if s[i:i+7] == "abbacca" or s[i:i+7] == "accabba":
            ans = min(ans, 7)
    
    if ans == 10**9:
        print(-1)
    else:
        print(ans)
