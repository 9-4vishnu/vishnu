import random
a=["rock","paper","scissor"]
computer_choice=random.choice(a)

player_score=0
computer_score=0

while True:
    player_choice=input("enter your choice:")
    if player_choice==computer_choice:
        print("Tie")
        player_score+=1
        computer_score+=1
    elif player_choice=="rock":
       if computer_choice=="paper":
           print("computer wins")
           computer_score+=1
       if computer_choice=="scissor":
           print("player wins")
           player_score+=1
    elif player_choice=="paper":
       if computer_choice=="scissor":
           print("computer wins")
       if computer_choice=="rock":
           print("player wins")
           player_score+=1
    elif player_choice=="scissor":
        if computer_choice=="rock":
            print("computer wins")
            computer_score+=1
        if computer_choice=="paper":
            print("player wins")
            player_score+=1
    else:
        print("final score")
        print("player_score:",player_score)
        print("computer_score:",computer_score)

        break