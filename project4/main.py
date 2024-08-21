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
game_images = [rock, paper, scissors]
user_choice = int(input("Choose between Rocks(0), paper(1), scissors(2)\n"))
print("YOU Have Chosen", game_images[user_choice])

comp_choice = random.randint(0, 2)
print("The Computer has Chosen",game_images[comp_choice])

if user_choice == 0:
    if comp_choice==1:
        print("YOU Lost")
    elif comp_choice == user_choice:
        print("It is a draw!")
    else:
        print("YOU WIN!")

elif user_choice == 1:
    if comp_choice==2:
        print("YOU Lost")
    elif comp_choice == user_choice:
        print("It is a draw!")
    else:
        print("YOU WIN!")

elif user_choice == 2:
    if comp_choice == 0:
        print("YOU Lost")
    elif comp_choice == user_choice:
        print("It is a draw!")
    else:
        print("YOU WIN!")
else:
    print("Invalid input")
