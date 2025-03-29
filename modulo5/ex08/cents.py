from enum import Enum

class InsufficientBalance(Exception):
    """Exceção lançada quando o saldo é insuficiente para realizar uma operação."""
    pass

class OperationType(Enum):
	DEPOSIT = "[+]"
	WITHDRAW = "[-]"

class Account:
	def __init__(self, account_id: float, *cpfs: str):
		self.account = account_id
		self.cpfs = cpfs
		self.__balance: float = 0.00
		self.__operations: list[str] = []

	def statement(self) -> None:
		string = "\n".join(self.__operations)
		return print(f"{string}\nBalance: R$ {self.__balance:,.2f}")

	def deposit(self, amount: float, description: str) -> None:
		if amount < 0:
			print("Valor deve ser > 0")
			raise ValueError
		self.__balance += (amount / 100)
		print(OperationType.DEPOSIT.value, self.account)
		self.__operations.append(f"[+] R$ {(amount / 100):,.2f} ({description})")

	def withdraw(self, amount: float, description: str) -> None:
		if amount / 100 < 0:
			print("Valor deve ser > 0")
			raise ValueError 
		if self.__balance - (amount / 100) < 0:
			print(f"Você não tem saldo suficiente. Balance: R$ {self.__balance}")
			raise ValueError
		self.__balance -= (amount / 100)
		print(OperationType.WITHDRAW.value, self.account)
		self.__operations.append(f"[-] R$ {(amount / 100):,.2f} ({description})")

	def __repr__(self) -> str:
		return f"Account({self.account}, ...)"

	def __str__(self) -> str:
		return f"Account: {self.account}\nBalance: R$ {self.__balance:,.2f}"

class Bank:
	def __init__(self):
		self.__accounts = {}

	def add_account(self, account: Account):
		self.__accounts[account.account] = account

	def get_account_by_cpf(self, acc_cpf: str) -> Account:
		for acc in self.__accounts.values():
			if acc.cpf == acc_cpf:
				return acc
		raise ValueError("Account cpf not find")

	def get_account_by_id(self, acc_id: int) -> Account:
		try:
			return self.__accounts[acc_id]
		except KeyError:
			raise ValueError("Account id not find")

	def transfer(self, source_id: int, destination_id: int, value: int, descripition: str) -> None:
		dest = self.get_account_by_id(destination_id)
		src = self.get_account_by_id(source_id)
		src.withdraw(value, descripition)
		dest.deposit(value, descripition)

	def __len__(self) -> int:
		return len(self.__accounts)

	def __contains__(self, id: int) -> bool:
		if id in self.__accounts:
			return True
		return False

	def __getitem__(self, id: int) -> Account:
		try:
			return self.get_account_by_id(id)
		except KeyError:
			raise ValueError("Account id not find")

