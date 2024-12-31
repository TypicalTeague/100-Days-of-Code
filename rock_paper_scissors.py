import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0,2)
if user > 2 or user < 0:
    print("Invalid number. You lose")
elif user == 2 and computer == 0:
    print(rock_paper_scissors[user])
    print("Computer chose:\n", rock_paper_scissors[computer])
    print("You lose")
elif computer == 2 and user == 0:
    print(rock_paper_scissors[user])
    print("Computer chose:\n",rock_paper_scissors[computer])
    print("You win")
elif user > computer:
    print(rock_paper_scissors[user])
    print("Computer chose:\n",rock_paper_scissors[computer])
    print("You win")
elif computer > user:
    print(rock_paper_scissors[user])
    print("Computer chose:\n", rock_paper_scissors[computer])
    print("You lose")
elif computer == user:
    print(rock_paper_scissors[user])
    print("Computer chose:\n", rock_paper_scissors[computer])
    print("You tie")
