class MyCircularDeque(object):

    def __init__(self, k):
        self.k=k
        self.q=[0]*k
        self.front=0
        self.rear=0
        self.size=0

    def insertFront(self, value):
        if self.size==self.k:
            return False
        self.front=(self.front-1)%self.k
        self.q[self.front]=value
        self.size+=1
        return True

    def insertLast(self, value):
        if self.size==self.k:
            return False
        self.q[self.rear]=value
        self.rear=(self.rear+1)%self.k
        self.size+=1
        return True

    def deleteFront(self):
        if self.size==0:
            return False
        self.front=(self.front+1)%self.k
        self.size-=1
        return True

    def deleteLast(self):
        if self.size==0:
            return False
        self.rear=(self.rear-1)%self.k
        self.size-=1
        return True

    def getFront(self):
        if self.size==0:
            return -1
        return self.q[self.front]

    def getRear(self):
        if self.size==0:
            return -1
        return self.q[(self.rear-1)%self.k]

    def isEmpty(self):
        return self.size==0

    def isFull(self):
        return self.size==self.k
    

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()