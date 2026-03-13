import random

list1 = ['rock','paper','scissor']
rounds =10
comp_score =0
user_score =0
while rounds>0:
 comp_choice= random.choice(list1)
 user_choice=input("Enter yours choice rock, paper, scissor: ").lower()
 if comp_choice == user_choice:
    print('tie')
 elif comp_choice == "scissor" and user_choice == "rock":
        print("you won")
        user_score+=1
 elif comp_choice == "rock"and user_choice =="paper":
         print("you won")
         user_score+=1
 elif comp_choice=="paper" and user_choice=="scissor":
         print("you won")
         user_score+=1
 elif user_choice not in list1:
        print("invalid choice")
 else:
        print("you lose")
        comp_score +=1
 print("comp_choice was ",comp_choice)
 print("user_choice was",user_choice)
 rounds-=1
 print("remaing round",rounds)