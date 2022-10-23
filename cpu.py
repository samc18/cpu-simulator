from cache import Cache
from memory import Memory

class CPU:
    def __init__(self):
        self.cpu_counter = 0
        self.registers = [0] * 9
        self.cache_flag = False
        self.cache = Cache()
        self.memory_bus = Memory()

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def reset_cpu_counter(self):
        self.cpu_counter = 0

    def set_cpu_counter(self, value):
        self.cpu_counter = value

    def get_cpu_counter(self):
        return self.cpu_counter

    def reset_registers(self):
        for i in range(len(self.registers)):
            self.registers[i] = 0
        
    def set_cache_flag(self, value):
        self.cache_flag = value

    # Cache operations

    def flush_cache(self):
        self.cache.flush_cache()

    def search_cache(self, address):
        return self.cache.search_cache(address)

    def write_cache(self, address, value):
        self.cache.write_cache(address, value)

    # Memory operations

    def search_memory_bus(self, address):
        return self.memory_bus.search_memory_bus(address)

    def write_memory_bus(self, address, value):
        self.memory_bus.write_memory_bus(address, value)

    # Instructions implementations

    def jump_instruction(self, target):
        self.cpu_counter = int(target)

    def add_instruction(self, destination, source, target):
        self.registers[int(destination[1:])] = self.registers[int(source[1:])] + \
        self.registers[int(target[1:])]

    def add_i_instruction(self, destination, source, immediate):
        self.registers[int(destination[1:])] = self.registers[int(source[1:])] + \
            int(immediate)

    def cache_instruction(self, value):
        if value == 0:
            self.set_cache_flag(False)
        if value == 1:
            self.set_cache_flag(True)
        if value == 2:
            self.flush_cache()

    def parse_instruction(self, instruction):
        instruction_parsed = instruction.split(',')
        self.increment_cpu_counter()
        if instruction_parsed[0] == 'ADD':
            self.add_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == 'ADDI':
            self.add_i_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == 'J':
            self.jump_instruction(instruction_parsed[1])
        if instruction_parsed[0] == 'CACHE':
            self.cache_instruction(instruction_parsed[1])