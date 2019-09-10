#!/usr/bin/env python3

class mg_queue:
    def __init__(self):
        self.l=[]

    def empty(self):
        """
        return True, if the queue is empty.
        return False, if the queue is no empty.
        """
        return len(self.l) == 0

    def put(self, item):
        return self.l.append(item)

    def get(self):
        if not self.empty():
            return self.l.pop(0)
        else:
            return None

    def peek(self):
        """
        return the head without pop.
        """
        if not  self.empty():
            return self.l[0]
        else:
            return None

if __name__ == "__main__":
    q=mg_queue()
    q.put(1)
    print(q.peek())
    q.put(2)
    print(q.get())
    print(q.get())
