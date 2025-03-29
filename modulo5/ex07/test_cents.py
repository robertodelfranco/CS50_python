# >>> from operation import Account, InsufficientBalance
# >>> conta = Account(123, "cpf1", "cpf2")
# >>> # Realiza algum depósito para definir um saldo, se necessário
# >>> conta.deposit(1000, "Depósito inicial")
# >>> # Tenta realizar um saque que pode causar a exceção
# >>> try:
# ...     conta.withdraw(5000, "Saque")
# ... except InsufficientBalance as e:
# ...     print(f"Operação não permitida: {e}")