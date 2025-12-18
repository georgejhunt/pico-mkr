import gc
import micropython

gc.collect() # Force a garbage collection
print("--- Memory Report ---")
print(f"Allocated: {gc.mem_alloc()} bytes")
print(f"Free: {gc.mem_free()} bytes")
print("---------------------")
micropython.mem_info() # Prints a detailed summary

