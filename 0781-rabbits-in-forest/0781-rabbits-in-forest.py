class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        d={}
        for a in answers:
            d[a]=d.get(a,0)+1
        
        res=0
        for x,c in d.items():
            g=x+1
            res+=((c+g-1)//g)*g
        
        return res