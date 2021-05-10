# Kyle Ziegler 5/2021
# LRU cache implementation - using a hashmap and a deque (
# double ended queue)
# O(1) for all operations

import collections
  
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.linked_list = collections.deque()

    def get(self, key: int) -> int:
        print(self.linked_list)
        if(key in self.d):
            
            # print(key)
            # Move the item to the end of the list (most recently
            # accessed)
            self.linked_list.remove(key)
            self.linked_list.append(key)
            return self.d[key]
        else:
            # not found
            return -1

    def put(self, key: int, value: int) -> None:
        # print("put",key, value)
        if (len(self.d.keys()) == self.capacity):
            # Remove the oldest item

            print("We are full",self.capacity, key, self.linked_list)
            v = self.linked_list.popleft()
            self.d.pop(v)
        else:
            # There's room just store it in the dict 
            self.d[key] = value
    
        self.linked_list.append(key)
        return None