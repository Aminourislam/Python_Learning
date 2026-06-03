# Some Good Debuging techniques

# 1. print()

def add(a,b):
	result = a+b
	print(f"Adding {a} and {b} gives {result}")
	return result
add(1,2)

# 2. pdb module

import pdb 
def divide(a,b):
	pdb.set_trace()
	return a/b

divide(3,4)

# 3. IDE breakpoint

# ......