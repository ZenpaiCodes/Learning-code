# OOP
# 4 pillars of OOP
# 1. Abstraction - hiding the details of how something works.
# 2. Encapsulation - hiding the details of how something works.
# 3. Inheritance - subclassing
# 4. Polymorphism - using the same method name on different types of objects.

class PlayerCharacter:
    # self is refering to PlayerCharacter, that is being created.
    # This is a class attribute. It is shared by all instances of the class.
    membership = True

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def introduce_self(self):
        print(f"\nI am {self.name} and I am level {self.level}\n")


player1 = PlayerCharacter('Zulk', 100)
player2 = PlayerCharacter('Xeck', 89)
# adding a new attribute to the object outside class PlayerCharacter.
player2.AttackLevel = 80

# using the same class, object allocates in different memory locations.
print(player1)
print(player2)

player1.introduce_self()
player2.introduce_self()

print(
    f"Hi {player1.name}, your level is {player1.level}")
print(
    f"Hi {player2.name}, your level is {player2.level}, and your attack level is {player2.AttackLevel}")


# 2ND example
class user():
    def __init__(self, email):
        user.email = email
    def sign_in(self):
        print("You are logged in.")


class warrior(user):
    def __init__(self, name, power, skill, email):
        user.__init__(self, email) # calling the parent class __init__ method.
        self.name = name
        self.power = power
        self.skill = skill

    def attack(self):
        print(
            f"{self.name} attacks with {self.power} power.")


class wizard(user):
    def __init__(self, name, spell, skill, mana, email):
        user.__init__(self, email) # calling the parent class __init__ method.
        self.name = name
        self.mana = mana
        self.spell = spell
        self.skill = skill

    def attack(self):
        print(
            f"{self.name} attacks with {self.spell} spell: {self.mana} mana is used.")


class archer(user):
    def __init__(self, name, power, num_arrows):
        self.name = name
        self.power = power
        self.num_arrows = num_arrows

    def attack(self):
        print(
            f"{self.name} attacks with {self.power} power. {self.num_arrows} left.")


warrior = warrior('Zulk', 99, 'fortify', 'zulk@email.com')
wizard = wizard('Xeck', 'fire Ball', 'ultra magic', 80,'Xeck@mail.com')

warrior.attack()
wizard.attack()


# player is a parameter. It is a variable to be used in the function.
def player_attack(player):
    player.attack()


# warrior is an argument. It is a variable to be used in the function.
player_attack(warrior)
print(dir(archer))
