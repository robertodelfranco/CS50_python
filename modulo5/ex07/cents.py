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
		print(OperationType.DEPOSIT.value)
		self.__operations.append(f"[+] R$ {(amount / 100):,.2f} ({description})")

	def withdraw(self, amount: float, description: str) -> None:
		if amount / 100 < 0:
			print("Valor deve ser > 0")
			raise ValueError 
		if self.__balance - (amount / 100) < 0:
			print(f"Você não tem saldo suficiente. Balance: R$ {self.__balance}")
			raise ValueError
		self.__balance -= (amount / 100)
		print(OperationType.WITHDRAW.value)
		self.__operations.append(f"[-] R$ {(amount / 100):,.2f} ({description})")

	def __repr__(self) -> str:
		return f"Account({self.account}, ...)"

	def __str__(self) -> str:
		return f"Account: {self.account}\nBalance: R$ {self.__balance:,.2f}"
