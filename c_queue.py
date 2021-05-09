# Author:
# Date:
# Title:
# Descirption: 
import heapq

# The standart class for PriorityQueue (in module queue), has bad implementation for put() function, like: put(priority1, priority2 ...), and then sort it.
# But in our case we need to put graph coordinates with some priority,like:                                put(item, priority), and this simple class can do this very good
class PriorityQueue:
    
    def __init__(self):
        self.data = []
        self.index = 0
        
    def put(self, item, priority):
        heapq.heappush(self.data, (priority, self.index, item))
        self.index += 1

    def get(self):
        return heapq.heappop(self.data)[-1]

    def top(self):
        if not self.empty():
            return self.data[0]
        return (0, 0, (float("inf"), float("inf")))
    
    def remove(self, item):
        if item in self.data:
            self.data.remove(item)

    def empty(self):
        return True if len(self.data) == 0 else False

if __name__ == "__main__":
    print("Try main.py...")