rock_sign = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper_sign = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors_sign = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
options = [rock_sign,paper_sign,scissors_sign]

print("Let's play rock, paper, scissors. Loser is a stinky frog!\n")

computer = random.choice(options)
player_1 = input("What will you chose: rock, paper or scissors? ")

if player_1 == "paper":
    player_1 = paper_sign
if player_1 == "rock":
    player_1 = rock_sign
if player_1 == "scissors":
    player_1 = scissors_sign

print(f'\nYour choice is: {player_1}')
print(f'My pick is: {computer}')

if player_1 == computer:
    print("It\'s a draw!")
elif player_1 == rock_sign and computer == scissors_sign:
    print("You won this one!")
elif player_1 == rock_sign and computer == paper_sign:
    print("JAJAJJAJA you are a stinky frog!")
elif player_1 == paper_sign and computer == scissors_sign:
    print("JAJAJJAJA you are a stinky frog!")
elif player_1 == paper_sign and computer == rock_sign:
    print("Your won this one!")
elif player_1 == scissors_sign and computer == rock_sign:
    print("JAJAJJAJA you are a stinky frog!")
elif player_1 == scissors_sign and computer == paper_sign:
    print("Your won this one!")
