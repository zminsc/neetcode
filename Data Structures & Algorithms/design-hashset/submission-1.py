NUM_BUCKETS = 10000

def hash(key: int) -> int:
    return key % NUM_BUCKETS

class LinkedListNode:
    def __init__(self, val: int, prev: Node | None = None):
        self.val = val
        self.prev = None
        self.next = None

class MyHashSet:

    def __init__(self):
        self.arr = [None] * NUM_BUCKETS

    def add(self, key: int) -> None:
        currNode = self.arr[hash(key)]
        if currNode is None:
            self.arr[hash(key)] = LinkedListNode(key)
            return
        while currNode is not None:
            if currNode.val == key:
                return
            if currNode.next is None:
                currNode.next = LinkedListNode(key, currNode)
                return
            currNode = currNode.next

    def remove(self, key: int) -> None:
        currNode = self.arr[hash(key)]
        while currNode is not None:
            if currNode.val == key:
                if currNode.prev is None and currNode.next is None:
                    self.arr[hash(key)] = None
                elif currNode.prev is None:
                    self.arr[hash(key)] = currNode.next
                elif currNode.next is None:
                    currNode.prev.next = None
                else:
                    currNode.prev.next = currNode.next
                    currNode.next.prev = currNode.prev
                return
            else:
                currNode = currNode.next

    def contains(self, key: int) -> bool:
        currNode = self.arr[hash(key)]
        while currNode is not None:
            if currNode.val == key:
                return True
            currNode = currNode.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)