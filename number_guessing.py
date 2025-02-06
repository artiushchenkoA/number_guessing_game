import sys
import random

def select_difficulty():
    print('''Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n''')    

    while True: 
        choise = int(input('Enter your choise: 1, 2 or 3: ').strip())
        match choise:
            case 1: return 10
            case 2: return 5
            case 3: return 3
            case default: print('Invalid input.')

def set_random_number():
    return random.randint(1,100)

def prompt_guess(prompt, input_func = input):
    while True: 
        try:
            guess = int(input_func(prompt).strip())
            if guess < 1 or guess > 100:
                print('Invalid input.')
                continue
            return guess
        except ValueError:
            print('Invalid input')

def evaluate_input(number, difficulty):
    count = 1
    while count <= difficulty:
        guess = prompt_guess('Guess your number: ')
        if guess < number:
            print('Incorrect! The number is greater than %d.\n' % guess)
            count = count + 1
        elif guess > number:
            print('Incorrect! The number is less than %d.\n' % guess)
            count = count + 1
        else :
            print('Congratulations! You guessed the correct number in %d attempts.' % count)
            sys.exit()
    if count > difficulty:
        print('You lost.')


def main():
    while True: 
        difficulty = select_difficulty()
        number = set_random_number()
        evaluate_input(number, difficulty)

        play_again = input("Would you like to start over? (y /n): ").strip().lower()
        if play_again != 'yes':
            print('Bye.')
            sys.exit()
    

if __name__ == '__main__':
    main()