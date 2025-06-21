import random
choices=["rock","paper","scissor"]
user_choice=input("enter choices(rock,paper,scissor:")
computer_choice=random.choice(choices)
win_count=0
loss_count=0
print(f"Computer chose: {computer_choice}")

if computer_choice==user_choice :
    print("game is tied")
elif computer_choice=='paper' and user_choice=='scissor' :
    print("scissor cut paper | user win!")
elif computer_choice=='paper' and user_choice=='rock' :
    print("paper close rock | you lose!")
elif computer_choice == 'scissor' and user_choice == 'rock':
    print("rock destroy scissor| you win !")
elif computer_choice == 'scissor' and user_choice == 'paper':
    print("scissor cut paper | user lose!")
elif computer_choice=='rock'  and user_choice=='paper':
    print("paper close rock | you win!")
elif user_choice in choices:
    print("You lose!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")
