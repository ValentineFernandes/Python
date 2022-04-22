"""Rock, Paper, Scissors, by Odysy Academy
The classic hand game of luck.
Tags: short, game"""
import random, time, sys, os
print('''Rock, Paper, Scissors, by Arsen, Odysy Academy 
 - Rock beats scissors.
 - Paper beats rocks.
 - Scissors beats paper.
 ''')

 # These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # Main game loop.
    while True: # Keep asking until player enters R, P, S, or Q.
        print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
        print('Enter your move: (R)ock (P)aper (S)cissors (L)izard (SP)ock or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing!')
            sys.exit()
        
        if playerMove == 'R' or playerMove == 'P' or playerMove == 'S' or playerMove == 'L' or playerMove == "SP":
            break
        else:
            print('Type one of R, P, S, L, SP or Q')

    # Display what the player chose:
    if playerMove == 'R':
        print('ROCK versus...')
        playerMove = 'ROCK'
    elif playerMove == 'P':
        print('PAPER versus...')
        playerMove = 'PAPER'
    elif playerMove == 'S':
        print('SCISSORS versus...')
        playerMove = 'SCISSORS'
    elif playerMove == 'L':
        print('LIZARD versus...')
        playerMove = 'LIZARD'
    elif playerMove == 'SP':
        print('SPOCK versus...')
        playerMove = 'SPOCK'

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display what the computer chose:
    randomNumber = random.randint(1, 5)
    if randomNumber == 1:
        computerMove = 'ROCK'
    elif randomNumber == 2:
        computerMove = 'PAPER'
    elif randomNumber == 3:
        computerMove = 'SCISSORS'
    elif randomNumber == 4:
        computerMove = 'LIZARD'
    elif randomNumber == 5:
        computerMove = 'SPOCK'
    print(computerMove)
    time.sleep(0.5)

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties = ties + 1
    elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'ROCK' and computerMove == 'LIZARD':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'PAPER' and computerMove == 'ROCK':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'PAPER' and computerMove == 'SPOCK':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'SCISSORS' and computerMove == 'LIZARD':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'LIZARD' and computerMove == 'SPOCK':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'LIZARD' and computerMove == 'PAPER':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'SPOCK' and computerMove == 'ROCK':
        print('You win!')
        wins = wins + 1
        if wins >= 2:
            os.system('echo "SPOCK BEAST MODE ACTIVATED =>" $SECRET')
    elif playerMove == 'SPOCK' and computerMove == 'SCISSORS':
        print('You win!')
        wins = wins + 1

    elif playerMove == 'ROCK' and computerMove == 'PAPER':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'ROCK' and computerMove == 'SPOCK':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'PAPER' and computerMove == 'LIZARD':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'SCISSORS' and computerMove == 'SPOCK':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'LIZARD' and computerMove == 'SCISSORS':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'LIZARD' and computerMove == 'ROCK':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'SPOCK' and computerMove == 'PAPER':
        print('You lose!')
        losses = losses + 1
        if losses >= 2:
            os.system('echo "SPOCK RAGE MODE ACTIVATED =>" $SECRET')
    elif playerMove == 'SPOCK' and computerMove == 'LIZARD':
        print('You lose!')
        losses = losses + 1