t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    casinos = []
    
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append([l, r, real])
    
    changed = True
    while changed:
        changed = False
        best_index = -1
        best_real = k
        
        for idx, (l, r, real) in enumerate(casinos):
            if l <= k <= r and real > best_real:
                best_real = real
                best_index = idx
        
        if best_index != -1:
            k = casinos[best_index][2]
            casinos.pop(best_index)
            changed = True
    
    print(k)
