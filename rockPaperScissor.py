import random
from termcolor import colored
win, score= 0,0
print(colored("-------------Wecome to Rock, Paper, Scissor Game-------------","blue"))
shapes = ['rock','paper','scissor']


def user_choice(user_inp):
    ai = random.choice(shapes)
    user_input = shapes[int(user_inp)-1]

    print(f'Yours {user_input} || Computer {ai}')

    if user_input == "paper" and ai == "scissor" or \
            user_input == "scissor" and ai == "rock" or \
            user_input == "rock" and ai=="paper":
        return "loose"

    elif user_input == "rock" and ai == "scissor" or \
            user_input == "scissor" and ai=="paper" \
            or user_input == "paper" and ai=="rock":
        return "win"

    else:
        return "playagain"

run = True

while run:
    print(colored(f"-------------Score: {score} --------------------------------", "blue"))
    print(colored("Choose: 1.Rock || 2.paper || 3.Scissor","yellow"))
    user_inp = input("> ").lower()
    if user_inp.isdigit():
        if int(user_inp) <=3:
            result = user_choice(user_inp)
            if result=="win":
                win = 1
                score +=win
                print(colored("You win","green"))

            elif result=="loose":
                print(colored("You loose","red"))
            elif result == "playagain":
                print(colored('Play again!','green'))
        else:
            print(colored("Invalid Entry, please try again!",'red'))
    else:
        print(colored("Invalid Entry, please try again!",'red'))
