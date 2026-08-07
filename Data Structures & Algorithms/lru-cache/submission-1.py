class Node:
     def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node):
       prev = node.prev
       nxt = node.next
       prev.next = nxt
       nxt.prev = prev
    
    def insert(self, node: Node): # we insert at right
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
        
    def get(self, key: int) -> int: # we get key and update the LRU
        if key in self.cache:
            self.remove(self.cache[key]) # remove to so to ove to front
            self.insert(self.cache[key]) # move to recently used to the right
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            

        
