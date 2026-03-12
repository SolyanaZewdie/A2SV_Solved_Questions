class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.h=[homepage]
        self.i=0
        self.end=0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.i+=1
        if self.i<len(self.h):
            self.h[self.i]=url
        else:
            self.h.append(url)
        self.end=self.i

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.i=max(0,self.i-steps)
        return self.h[self.i]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.i=min(self.end,self.i+steps)
        return self.h[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)