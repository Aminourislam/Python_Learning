"""
Function Demonstration
----------------------
This program demonstrates two types of functions:
1. A function with a conditional return (New Year countdown)
2. A function that returns a value
"""

def new_year(wishes=True):
    """Countdown to New Year with optional Happy New Year message"""
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year!")

def boring_function():
    """Return a value (123)"""
    return 123

print("=== New Year Function Demo ===")
print("\nCalling new_year() with default parameter (wishes=True):")
new_year()

print("\nCalling new_year(False) - no Happy New Year message:")
new_year(False)

print("\n=== Return Value Function Demo ===")
x = boring_function()
print("The boring_function has returned its result. It's:", x)