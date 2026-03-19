import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    output = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        a = [int(x) for x in input_data[ptr:ptr+n]]
        ptr += n
        
        if n < 3:
            output.append("0")
            continue
            
        maxv = a[-1]
        ans = 0
        
        for k in range(2, n):
            ak = a[k]
            limit = ak if ak > maxv - ak else maxv - ak
            
            if a[k-1] + a[k-2] <= limit:
                continue
            
            i = 0
            j = k - 1
            while i < j:
                if a[i] + a[j] > limit:
                    ans += (j - i)
                    j -= 1
                else:
                    i += 1
                    
        output.append(str(ans))
    
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()