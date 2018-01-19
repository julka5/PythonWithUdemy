from player import Player
from enemy import Enemy, Troll, Vampire, VampireKing

julka = Player("Julka")

ugly_troll = Troll("Ug")
print(ugly_troll)

another_troll = Troll("Bum")
print(another_troll)

ugly_troll.grunt()
another_troll.grunt()


scary_vampire = Vampire("John")

while scary_vampire._alive:
    scary_vampire.take_damage(1)


king = VampireKing("Arthur")
print(king)
while king._alive:
    king.take_damage(25)