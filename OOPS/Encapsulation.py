
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(5000)
acc.deposit(2000)
print(acc.get_balance())   # ✅ 7000
print(acc.__balance)



#         class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Private property

# p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.__age)