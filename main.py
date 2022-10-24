from cpu import CPU

def fetch_instructions():
    instruction_file = open('instruction_input.txt', 'r')
    instructions = instruction_file.readlines()
    instructions = list(map(lambda s : s.strip(), instructions))
    return instructions

def fetch_data():
    data_file = open('data_input.txt', 'r')
    data = data_file.readlines()
    data = list(map(lambda s : s.strip(), data))
    return data

def initialize_memory_bus(cpu):
    data_loaded = fetch_data()
    for data in data_loaded:
        data_parsed = data.split(',')
        cpu.write_memory_bus(data_parsed[0], data_parsed[1])

def initialize_cache(cpu):
    data_loaded = fetch_data()
    for data in data_loaded:
        data_parsed = data.split(',')
        cpu.write_cache(data_parsed[0], data_parsed[1])

def send_instructions_to_cpu(cpu):
    instructions_loaded = fetch_instructions()
    for instruction in instructions_loaded:
        cpu.parse_instruction(instruction)

def display_memory():
    data_loaded = fetch_data()
    list = ''
    for data in data_loaded:
        data_parsed = data.split(',')
        list += f'Address: {data_parsed[0]} - Value: {my_cpu.memory_bus.memory_bus.get(data_parsed[0])} \n'
    return list.strip()

def display_cache():
    list = ''
    for i in range(len(my_cpu.cache.cache)):
        list += f'Address: {my_cpu.cache.cache[i][0]} - Value: {my_cpu.cache.cache[i][1]} \n'
    return list.strip()

def display_registers():
    list = ''
    for i in range(len(my_cpu.registers)):
        list += f'Register {i}: {my_cpu.registers[i]} \n'
    return list.strip()

my_cpu = CPU()

print('------------------------------')
print('Welcome to the CPU Simulator')
print('------------------------------')

print('Initializing memory bus...')
initialize_memory_bus(my_cpu)
initialize_cache(my_cpu)

print('------------------------------')
print('Memory addresses with value:')
print(display_memory())

print('------------------------------')
print('Cache:')
print(display_cache())

print('------------------------------')
print('Registers:')
print(display_registers())

print('------------------------------')
print('Sending instructions to CPU...')
send_instructions_to_cpu(my_cpu)

print('------------------------------')
print('Registers:')
print(display_registers())