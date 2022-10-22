memory_bus_size = 128

class Memory:
    def __init__(self):
        self.memory_bus = {}
        self.init_memory_bus()
        
    def init_memory_bus(self):
        for i in range(memory_bus_size):
            self.memory_bus['{0:08b'.format(i)] = 0

    def search_memory_bus(self, address):
        if self.memory_bus.get(address) == None:
            return None
        return self.memory_bus.get(address)

    def write_memory_bus(self, address, data)
        if self.memory_bus.get(address) == None:
            return
        self.memory_bus[address] = data