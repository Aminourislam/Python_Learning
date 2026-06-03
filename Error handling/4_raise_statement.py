# raise statement

# def check_age(age):
# 	if age < 0:
# 		raise ValueError('Age cannot be negative!')
# 	return age

# try:
# 	check_age(-2)
# except ValueError as e:
# 	print(f"Error: {e}")

def process_data(data):
	try:
		result = int(data)
		return data*2
	except ValueError:
		print("Logging: Invalid data recevied")
		raise

try:
	process_data('abc')
except ValueError:
	print('Handled at high level')

#### Custom Exception handling 
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')
