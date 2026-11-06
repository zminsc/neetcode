class Node:
    def __init__(self, val: int):
        self.val = val
        self.prv = None
        self.nxt = None

class MyHashSet:

    def __init__(self):
        self.buckets = 10000
        self.table = [None] * self.buckets
    
    def hash(self, key: int) -> int:
        return key % self.buckets

    def add(self, key: int) -> None:
        startNode = self.table[self.hash(key)]
        newNode = Node(key)
        if startNode is None:
            self.table[self.hash(key)] = newNode
        while startNode:
            if startNode.val == key:
                return
            if startNode.nxt is None:
                startNode.nxt = newNode
                newNode.prv = startNode
                return
            startNode = startNode.nxt
        

    def remove(self, key: int) -> None:
        startNode = self.table[self.hash(key)]
        while startNode:
            if startNode.val == key:
                if startNode.prv is None and startNode.nxt is None:
                    self.table[self.hash(key)] = None
                elif startNode.prv is None:
                    self.table[self.hash(key)] = startNode.nxt
                elif startNode.nxt is None:
                    startNode.prv.nxt = None
                else:
                    startNode.prv.nxt = startNode.nxt
                    startNode.nxt.prv = startNode.prv
                print(self.table[self.hash(key)])
                return
            startNode = startNode.nxt

    def contains(self, key: int) -> bool:
        startNode = self.table[self.hash(key)]
        while startNode:
            if startNode.val == key:
                return True
            startNode = startNode.nxt
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)