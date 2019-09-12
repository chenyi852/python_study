#!/usr/bin/env python3
from queue import Queue 

class taskq():
    def __init__(self):
        self.q=Queue(128)
        self.consume_hook = None

    def produce(self, data):
        self.q.put(data)

    def consume(self):
        if not self.q.empty():
            msg = self.q.get()
            self.consume_hook(msg)

    def register_consume_hook(self, consume_hook):
        self.consume_hook = consume_hook

def process_data(data):
    print(data)

if __name__ ==  "__main__":
    t = taskq()
    t.register_consume_hook(process_data)
    msg1="ci fail"
    msg2="compile sucessfully"
    t.produce(msg1)
    t.produce(msg2)
    t.consume()
    t.consume()
