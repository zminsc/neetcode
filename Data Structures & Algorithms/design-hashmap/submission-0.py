NUM_BUCKETS = 10000

def hash(key: int) -> int:
    return key % NUM_BUCKETS

class LinkedListNode:
    def __init__(self, key: int, val: int, prev: Node | None = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class MyHashMap:

    def __init__(self):
        self.arr = [None] * NUM_BUCKETS

    def put(self, key: int, value: int) -> None:
        currNode = self.arr[hash(key)]
        if currNode is None:
            self.arr[hash(key)] = LinkedListNode(key, value)
            return
        while currNode is not None:
            if currNode.key == key:
                currNode.val = value
                return
            if currNode.next is None:
                currNode.next = LinkedListNode(key, value, currNode)
                return
            currNode = currNode.next

    def get(self, key: int) -> int:
        currNode = self.arr[hash(key)]
        while currNode is not None:
            if currNode.key == key:
                return currNode.val
            currNode = currNode.next
        return -1

    def remove(self, key: int) -> None:
        currNode = self.arr[hash(key)]
        while currNode is not None:
            if currNode.key == key:
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


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)