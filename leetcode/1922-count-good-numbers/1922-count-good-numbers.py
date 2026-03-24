class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        def power(base, exp):
            if exp == 0:
                return 1
            
            half = power(base, exp // 2)
            result = (half * half) % MOD
            
            if exp % 2 == 1:
                result = (result * base) % MOD
            
            return result
        
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        part1 = power(5, even_positions)
        part2 = power(4, odd_positions)
        
        return (part1 * part2) % MOD