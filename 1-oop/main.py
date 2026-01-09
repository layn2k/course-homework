class BankAccount:
    accounts = []

    def __init__(self, owner, account_number, balance: int = 0):
        if isinstance(owner, str):
            self.owner = owner
        else:
            raise ValueError("Некорректное имя владельца")
        if isinstance(account_number, (int, str)):
            self.account_number = account_number
        else:
            raise ValueError("Некорректный номер аккаунта")
        if isinstance(balance, (int, float)) and balance >= 0:
            self.balance = balance
        else:
            raise ValueError("Некорректное значение баланса")
        self.accounts.append(self)

    @classmethod
    def get_accounts_created(cls):
        return len(BankAccount.accounts)

    def deposit(self, amount):
        if isinstance(amount, (int, float)):
            self.balance += amount
        else:
            raise ValueError("Некорректная сумма пополнения")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)):
            if amount <= self.balance:
                self.balance -= amount
            else:
                return "На счете недостаточно средств."
        else:
            raise ValueError("Некорректная сумма пополнения")

    def transfer_to(self, other_account, amount):
        if isinstance(amount, (int, float)):
            if amount <= self.balance:
                target_account = next(
                    (
                        acc
                        for acc in BankAccount.accounts
                        if (acc.owner == other_account.owner)
                        and (acc.account_number == other_account.account_number)
                    ),
                    None,
                )
                if target_account:
                    self.balance -= amount
                    target_account.balance += amount
                else:
                    return "Счет получателя не найден."
            else:
                return "На счете недостаточно средств."
        else:
            raise ValueError("Некорректная сумма перевода")

    @property
    def info(self):
        return f"Имя владельца: {self.owner} - Номер счета: {self.account_number} - Баланс: {self.balance}"
