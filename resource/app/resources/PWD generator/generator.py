# Imports
from passwordmeter import test
from random import choice, randint

# Generator
words = open('words.txt', 'r').read().split('\n')
special_chars = ['!', '?', '%', '$', '*', '(', ')', '&', '@', '#', '^', '+', '=', '-', '_']

def create_password(num_words=2, num_numbers=4, num_special=3):
    """
    Generates Pasword out of User Input in the main window for the generator
    """
    #TODO Connect the arguments with wx for user customization.
    pass_str = ' '
    for _ in range(num_words):
        pass_str+=choice(words).lower().capitalize()
    for _ in range(num_numbers):
        pass_str+=str(randint(0,100))
    for _ in range(num_special):
        pass_str+=choice(special_chars)
    return pass_str

def main():
    pass_str=create_password()
    strength,_=test(pass_str)
    print('\nPassword: %s'%pass_str)
    print('Strength: %0.5f'%strength)

if __name__ == '__main__':
    main()
