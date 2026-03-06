class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                val = 1
            else:
                val = -1
            diff[start] += val
            diff[end + 1] -= val

        res = []
        cur = 0

        for i in range(n):
            cur += diff[i]
            shift = cur % 26
            c = ord(s[i]) - ord('a')
            c = (c + shift) % 26
            res.append(chr(c + ord('a')))

        return "".join(res)
