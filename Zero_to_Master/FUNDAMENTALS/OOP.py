# OOP

class PlayerCharacter:
    # self is refering to PlayerCharacter, that is being created.
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def run(self):
        print('run')


player1 = PlayerCharacter('Zulk', 100)

player2 = PlayerCharacter('Xeck', 89)
player2.AttackLevel = 80  # adding a new attribute to the object.

# using the same class, object allocates in different memory locations.
print(player1)
print(player2)

print(f"Hi {player1.name}, your level is {player1.level}")
print(f"Hi {player2.name}, your level is {player2.level}, and your attack level is {player2.AttackLevel}")

  
