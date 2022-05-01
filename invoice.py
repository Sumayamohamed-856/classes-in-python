class Invoice:
    def greeting(self):
        return 'hi there'

inv_one = Invoice()
print(inv_one.greeting())


class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def formatter(self):
    return f'{self.client} owes: ${self.total}'


# google = Invoice('Google', 100)
# snapchat = Invoice('SnapChat', 200)

# print(google.formatter())
# print(snapchat.formatter())

google = Invoice('Google', 100)

print(google.client)
# print(google.total)
google.client = 'yahoo'
print(google.client)


# How to Work with Python Properties and Decorators

class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total

google = Invoice('Google', 100)

print(google.client)

print(google.formatter())

google.client = 'Yahoo'

print(google.client)


class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def __str__(self):
     return f"Invoice from {self._client} for {self._total}"

inv = Invoice('google', 500)
print(str(inv))

# Repr

class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

  def __repr__(self):
    return f"Invoice({self.client}, {self.total})"


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))

# How to Build a Custom Iterator Class in Python

# class Lineup:

#     def __init__(self, players):
#         self.players = players

#     def __iter__(self):
#       self.n = 0
#       return self

#     def __next__(self):
#          if self.n < (len(self.players) -1):
#             player = self.players[self.n]
#             self.n += 1
#             return player
#          elif self.n == len(self.players[self.n] - 1):
#             player = self.players[self.n]
#             self.n += 0
#             return player

# astros = [
#   'Springer',
#   'Bregman',
#   'Altuve',
#   'Correa',
#   'Reddick',
#   'Gonzalez',
#   'McCann',
#   'Davis',
#   'Tucker'
# ]


# astros_lineup = Lineup(astros)
# process = iter(astros_lineup)

# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))
# print(next(process))

# proper method


class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:
            player = self.get_player(self.n)
            self.n = 0
            return player


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))


# Overview of Iterators vs Generators in Python

class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
     lineup_max = len(self.players)
     idx= 0


     while True:
            if idx < lineup_max:
                yield self.players[idx]
            else:
                idx = 0
                yield self.players[idx]

            idx += 1

    def __repr__(self):
        return f'InfiniteLineup({self.players})'

    def __str__(self):
        return  f"InfiniteLineup with the players: {', '.join(self.players)}"





astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()

print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(full_lineup))

print(str(full_lineup))