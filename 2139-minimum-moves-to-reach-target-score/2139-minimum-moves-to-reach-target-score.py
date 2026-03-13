class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        moves=0
        while target>1 and maxDoubles>0:
            if target%2:
                target-=1
            else:
                target//=2
                maxDoubles-=1
            moves+=1
        if target>1:
            moves+=target-1
        return moves