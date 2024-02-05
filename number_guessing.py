import math
import random

print('Welcome to the number guessing game');

lower_bound = int(input('Enter the lower bound: '));
higher_bound = int(input('Enter the high bound: '));

num_guesses = round(math.log2(higher_bound - lower_bound + 1));

print(f'\nWith the range {lower_bound,higher_bound}, YOU HAVE {num_guesses} GUESSES');

random_number = random.randint(lower_bound, higher_bound);
count = 0;
while num_guesses != 0:
    print(f'Remaining guesses: {num_guesses}');
    guess = int(input('\nEnter your guess: '));
    num_guesses -= 1;
    count += 1;
    if(guess == random_number):
        print(f'Congrats! You did it with {count} tries');
        break  
    elif(guess > random_number):
        print('Too high')
    else:
        print('Too Low')

if(num_guesses <= 0):
    print(f'\nThe number was {random_number}.\nBetter luck next time!')