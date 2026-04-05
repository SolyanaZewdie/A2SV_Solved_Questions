class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        children = [0] * k
        self.result = float('inf')
        def backtrack(index):
            if index == len(cookies):
                self.result = min(self.result, max(children))
                return
            
            for i in range(k):
                children[i] += cookies[index]

                if children[i] < self.result:
                    backtrack(index + 1)

                children[i] -= cookies[index]

                if children[i] == 0:
                    break

        backtrack(0)
        return self.result
