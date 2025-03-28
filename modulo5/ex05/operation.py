

class Operation:
	def __init__(self, cents: int, op_type: str, description: str):
		if cents <= 0:
			raise ValueError
		self.cents = cents
		self.op_type = op_type
		self.description = description

	def __repr__(self):
		return f"Operation(cents={self.cents}, op_type='{self.op_type}', descripition='{self.description}')"

	def __str__(self):
		reais = self.cents / 100
		reais = f"R$ {reais:,.2f}"
		reais = str(reais).replace(",", "X").replace(".", ",").replace("X", ".")
		return f"[+] R$ {reais} ({self.description})"


# my_op = Operation(11_222_00, 'credit', 'ATM deposit')
# print(my_op)