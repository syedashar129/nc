class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Key : Node

        # dummy left and right nodes
        self.left = Node(0, 0)
        self.right = Node(0,0)

        # Link the dummy nodes
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            # if getting --> becomes most recently used
            # thus move it to the end of the list
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # if already ezisting remove it
            self.remove(self.cache[key])
        
        # create new cache entry and add it to the end
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # evict lru if exceeds capacity 
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node):
        # remove by connecting to futher one
        prev_node = node.prev
        next_node = node.next 

        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node):
        # insert into right
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node # going in order here left --> right
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node


        
