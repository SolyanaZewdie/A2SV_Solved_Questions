class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        d=0
        for x in logs:
            if x=="../":
                if d>0:
                    d-=1
            elif x!="./":
                d+=1
        return d