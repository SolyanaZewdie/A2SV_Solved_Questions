class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        result = []

        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]  


        for ch in count:
            result.append(ch * count[ch])

        return ''.join(result)
