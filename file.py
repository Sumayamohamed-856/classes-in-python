import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text Files: ", file)

        if fnmatch.fnmatch(file, "*.rb"):
            print("ruby Files: ", file)

        if fnmatch.fnmatch(file, "*.yml"):
            print("yml Files: ", file)

        if fnmatch.fnmatch(file, "*.py"):
            print("python Files: ", file)

list_files()


players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]


second_players_base = [player for player in players if fnmatchcase(player, "*2B")]

print(second_players_base)


# pretty price function 

def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01

    return int(gross_price) + extension


print(pretty_price(3.20, 99))
print(pretty_price(3.99, 0.20))
print(pretty_price(3.20, .95))
print(pretty_price(3, 95))
print(pretty_price(3, 2))
