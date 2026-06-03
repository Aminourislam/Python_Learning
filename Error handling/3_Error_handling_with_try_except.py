# Error_handling_with_try_except

# try:
# 	pass
# except Exception as e:
# 	raise
# else:
# 	pass
# finally:
# 	pass

try:
	print("x = 10/0")
	x = 10/0
except ZeroDivisionError:
	print("You can't divide by zero!")
else:
	# Runs if no exception is raised in the try block
	print("Division successfull: ",x)
finally:
	# This block always runs
	print('This block {finally} always runs.')


try:
	number = int('abc')
	result = 10/ number
except ValueError:
	print('That is not a valid number!')
except ZeroDivisionError:
	print("Can't divide by Zero!")


try:
	x = 1/0
except ZeroDivisionError as e:
	print(f"Error occurred: {e}")

# multiple exception in a single except
try:
	number = int(input("Enter a number: "))
	result = 10/ number
except (ValueError, ZeroDivisionError) as e:
	print(f"Error occurred: {e}")