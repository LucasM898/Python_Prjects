import random
print("All inputs must be lowercase")
isplaying = 1
valid_inputs = ['rock', 'paper', 'scissors']
while isplaying == 1:
    #lets the user choose to play multiple rounds
    valid_input = 0
    #invalid input handling for the user
    while valid_input == 0:
        comp = input("Type 'player' to play against another player, or 'computer' to play against the computer \n")
        #comp will be the variable whether to play against a computer or not. Couldnt think of better name.
        if comp == 'player' or comp == 'computer':
            valid_input = 1
            #breaks the loop, because it's a valid input
        else:
            print('Not a valid input, please try again')
            #keeps the loop repeating until user enters a valid input
    if comp == 'player':
        p1wins = 0
        p2wins = 0
        winner = 0
        while winner == 0:
            print(f'the score is: \n Player 1: {p1wins} \n Player 2: {p2wins}')
            p1_input_valid = 0
            p2_input_valid = 0
            while p1_input_valid == 0:
                p1_move = input('Player1, enter your move. \n')
                if p1_move in valid_inputs:
                    p1_input_valid = 1
                else:
                    print('enter a valid input')
            while p2_input_valid == 0:
                p2_move = input('Player2, enter your move. \n')
                if p2_move in valid_inputs:
                    p2_input_valid = 1
                else:
                    print('enter a valid input')
            if p1_move == 'rock':
                if p2_move == 'scissors':
                    p1wins += 1
                elif p2_move == 'paper':
                    p2wins += 1
            if p1_move == 'scissors':
                if p2_move == 'paper':
                    p1wins += 1
                elif p2_move == 'rock':
                    p2wins += 1
            if p1_move == 'paper':
                if p2_move == 'rock':
                    p1wins += 1
                elif p2_move == 'scissors':
                    p2wins += 1
            if p1wins == 2:
                winner = 1
            elif p2wins == 2:
                winner = 1
        if p1wins == 2:
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')
    if comp == 'computer':
        p1wins = 0
        computerwins = 0
        winner = 0
        while winner == 0:
            print(f'the score is: \n Player 1: {p1wins} \n Computer: {computerwins}')
            p1_input_valid = 0
            while p1_input_valid == 0:
                p1_move = input('Player1, enter your move. \n')
                if p1_move in valid_inputs:
                    p1_input_valid = 1
                else:
                    print('enter a valid input')
            randindex = random.randint(0,2)
            computer_move = valid_inputs[randindex]
            if p1_move == 'rock':
                if computer_move == 'scissors':
                    p1wins += 1
                elif computer_move == 'paper':
                    computerwins += 1
                else:
                    print('tie')
            if p1_move == 'scissors':
                if computer_move == 'paper':
                    p1wins += 1
                elif computer_move == 'rock':
                    computerwins += 1
                else:
                    print('tie')
            if p1_move == 'paper':
                if computer_move == 'rock':
                    p1wins += 1
                elif computer_move == 'scissors':
                    computerwins += 1
                else:
                    print('tie')
            if p1wins == 2:
                winner = 1
            elif computerwins == 2:
                winner = 1
        if p1wins == 2:
            print('Player 1 wins!')
        else:
            print('Computer wins!!')
    valid_input = 0
    while valid_input == 0:
        playagain = input('Do you want to play again? yes or no \n')
        if playagain == 'yes' or playagain == 'no':
            valid_input = 1
        else:
            print('invalid input, please try again')
    if playagain == 'no':
        isplaying = 0

