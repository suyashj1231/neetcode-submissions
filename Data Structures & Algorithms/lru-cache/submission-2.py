class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # we map key to Node
        self.left = Node(0,0) # LRU
        self.right = Node(0,0) # MRU
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: Node):
        pre = self.right.prev
        nxt = self.right

        pre.next = node
        nxt.prev = node

        node.next = self.right
        node.prev = pre
    
    def remove(self, node: Node):
        prev = node.prev
        nxt = node.next
       # prev and nxt now ppoint to each other
        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # we remove from LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
