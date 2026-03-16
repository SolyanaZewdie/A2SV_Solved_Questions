class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n=len(costs)
        for i in range(n):
            costs[i].append(costs[i][0]-costs[i][1])
        costs.sort(key=lambda x:x[2])
        res=0
        half=n//2
        for i in range(half):
            res+=costs[i][0]
        for i in range(half,n):
            res+=costs[i][1]
        return res