t = int(input())

for _ in range(t):
    s = input().strip()
    i = 0
    working = set()
    
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        
        length = j - i
        
        if length % 2 == 1:
            working.add(s[i])
        
        i = j
    
    print(''.join(sorted(working)))
