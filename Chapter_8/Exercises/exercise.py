# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]

# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

# for house in sorted(houses):
#     print(house)


# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]
#
# houses = set()
# for student in students:
#     houses.add(student["house"])

# for house in sorted(houses):
#     print(house)


# balance = 0


# def main():
#     print("Balance:", balance)


# if __name__ == "__main__":
#     main()


# balance = 0


# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)


# def deposit(n):
#     balance += n


# def withdraw(n):
#     balance -= n


# if __name__ == "__main__":
#     main()


# balance = 0


# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)


# def deposit(n):
#     global balance
#     balance += n


# def withdraw(n):
#     global balance
#     balance -= n


# if __name__ == "__main__":
#     main()


# class Account:
#     def __init__(self):
#         self._balance = 0

#     @property
#     def balance(self):
#         return self._balance

#     def deposit(self, n):
#         self._balance += n

#     def withdraw(self, n):
#         self._balance -= n


# def main():
#     account = Account()
#     print("Balance:", account.balance)
#     account.deposit(100)
#     account.withdraw(50)
#     print("Balance:", account.balance)


# if __name__ == "__main__":
#     main()


# MEOWS = 3

# for _ in range(MEOWS):
#     print("meow")


# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")


# cat = Cat()
# cat.meow()


# def meow(n):
#       for _ in range(n):
#           print("meow")


# number = input("Number: ")
# meow(number)


# def meow(n: int):
#     for _ in range(n):
#         print("meow")


# number = input("Number: ")
# meow(number)


# def meow(n: int):
#     for _ in range(n):
#         print("meow")


# number: int = input("Number: ")
# meow(number)


# def meow(n: int):
#     for _ in range(n):
#         print("meow")


# number: int = int(input("Number: "))
# meow(number)


# def meow(n: int):
#     for _ in range(n):
#         print("meow")


# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)


# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")


# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)


# def meow(n: int) -> str:
#     return "meow\n" * n


# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")


# def meow(n):
#     """Meow n times."""
#     return "meow\n" * n


# number = int(input("Number: "))
# meows = meow(number)
# print(meows, end="")


# def meow(n):
#     """
#     Meow n times.

#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n


# number = int(input("Number: "))
# meows = meow(number)
# print(meows, end="")


# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py [-n NUMBER]")


# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("-n")
# args = parser.parse_args()

# for _ in range(int(args.n)):
#     print("meow")


# import argparse

# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", help="number of times to meow")
# args = parser.parse_args()

# for _ in range(int(args.n)):
#     print("meow")


# import argparse

# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", default=1, help="number of times to meow", type=int)
# args = parser.parse_args()

# for _ in range(args.n):
#     print("meow")


# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# print(total(100, 50, 25), "Knuts")


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = [100, 50, 25]

# print(total(coins[0], coins[1], coins[2]), "Knuts")


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = [100, 50, 25]

# print(total(*coins), "Knuts")


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# print(total(galleons=100, sickles=50, knuts=25), "Knuts")


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts


# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(**coins), "Knuts")


# print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)


# def f(*args, **kwargs):
#     print("Positional:", args)


# f(100, 50, 25)


# def f(*args, **kwargs):
#     print("Named:", kwargs)


# f(galleons=100, sickles=50, knuts=25)




