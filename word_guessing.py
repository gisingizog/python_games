import random
fruits = ['Mango','Pineapple','Watermelon','Dragonfruit','Fig','Starfruit','Rambutan','Durian','Cherimoya','Passionfruit'];

cities = ['Tokyo','Berlin','Santorini','Rio de Janeiro','Kigali','Nairobi'];

print('Welcome to the word guessing game!!!')
choice = int(input('Choose the category of words to guess from: \n1. Fruits\n2. Cities\n\nAnswer:  '));

if(choice == 1):
    random_word = random.choice(fruits);
elif choice == 2:
    random_word = random.choice(cities);
else : 
    print('\nInvalid Response');

tries = len(random_word);
fails = 0;
guesses = '';
while tries > 0:
    print(f'\nRemaining tries: {tries}')
    guess = input('\nEnter the letter: ');
    guesses += guess;
    tries -= 1;
    for char in random_word:
        if char in guesses:
            print(char, end=' ');
        else:
            print('_',end=' ');
            fails += 1;

else:
    if guesses == random_word:
        print('\n\nCongrats!You won!')  
    else:
        print(f'\n\nYou lost!\nThe word was {random_word}');


