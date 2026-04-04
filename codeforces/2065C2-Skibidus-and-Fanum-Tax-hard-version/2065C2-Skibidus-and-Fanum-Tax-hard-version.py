import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        m = int(input[ptr+1])
        ptr += 2
        
        a = list(map(int, input[ptr : ptr + n]))
        ptr += n
        
        b = list(map(int, input[ptr : ptr + m]))
        ptr += m
        
        b.sort()
        
        prev = -float('inf')
        possible = True
        
        for x in a:
            v1 = x if x >= prev else float('inf')
            
            target = prev + x
            idx = bisect_left(b, target)
            
            v2 = float('inf')
            if idx < m:
                v2 = b[idx] - x
            
            best = min(v1, v2)
            
            if best == float('inf'):
                possible = False
                break
            prev = best
            
        results.append("YES" if possible else "NO")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()