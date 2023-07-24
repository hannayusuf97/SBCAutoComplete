import ctypes

# Open the game process
process_handle = ctypes.windll.kernel32.OpenProcess(0x10, False, 13932)

# Read the memory address containing the game variable
address = 0x12345678  # Replace this with the actual memory address

buffer = ctypes.create_string_buffer(4)  # Assuming the variable is an integer (4 bytes)
bytes_read = ctypes.c_ulong(0)

ctypes.windll.kernel32.ReadProcessMemory(process_handle, address, buffer, 4, ctypes.byref(bytes_read))

# Interpret the buffer as an integer and use the variable in your code
score = int.from_bytes(buffer.raw, byteorder='little')

print(f"The current score is: {score}")