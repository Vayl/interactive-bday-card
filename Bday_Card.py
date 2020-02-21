'''
This interactive, narrative driven brithday card includes a simple hangman mini-game and some ASCII art.
'''
import os, shutil, sys, time

# Initial screen clear
os.system('clear')

# GLOBALS
yes = ['yes', 'Yes', 'y', 'Y']
no = ['No', 'no', 'n', 'N']

# TYPEWRITER
def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        if char != '\n':
            time.sleep(0.08)
        else:
            time.sleep(0.8)

# GUARD CONVERSATION
def guard_convo():
    guard_play = False
    while guard_play is False:
        os.system('clear')
        typewriter('''
~~~ By the entrance of the majestic, but shut, stone door, a guard quietly and
methodically sharpens his knife.

As you get closer the young man lifts his cold, ice blue eyes and with them
touches your soul.

He measures you for a brief moment, then starts back on his blade.
''')
        talk_to_guard = input('\n~~~ Talk to the guard? ')
        if talk_to_guard in yes:
            os.system('clear')
            typewriter('''
"You have come a long way XXXXXX... if that is really you.
 How long has it been? More than a thousand years at least.
 If you truly are my old friend, none other than the XXXXXXX witch, you will know
 what this means..."

The young man points at a mysterious carving on top the old door...
''')
            game_start = input('\n~~~ Decypher the carving? ')
            if game_start in yes:
                os.system('clear')
                guard_play = True          
            else:
                os.system('clear') 
                guard_play = False
                
                
# HANGMAN MINI-GAME
def hangman():
    underscore = '_ '
    secret_word = 'mellon'

    # ['m', 'e', 'l', 'l', 'o', 'n']
    secret_lst = list(secret_word)

    # underscore list: ['_ ', '_ ', '_ ', '_ ', '_ ', '_ ']
    under_lst = []
    for element in secret_lst:
        under_lst.append('_ ')

    # visual representation: '_ _ _ _ _ _' 
    under_word = ' '.join(under_lst)

    # not working with under_lst seems to be the better choice (TBC)
    new_lst = under_lst

    # GAME START
    # cannot print out full word without underscore at the end of the loop
    while underscore in new_lst: 
        os.system('clear')
        
        clean_new_lst = ' '.join(new_lst) # constantly updated visual rep (is a string)
        
        columns = shutil.get_terminal_size().columns # center visual rep
        print()
        print(clean_new_lst.center(columns))
        
        guess = input('\nTake a guess, one letter at a time: ' )
        for element in range(len(secret_lst)):
            if guess == secret_lst[element]:
                new_lst[element] = secret_lst[element] # update new_lst, change reflects in clean_new_lst
            else:
                continue
    os.system('clear')


# MANUSCRIPT
def manuscript():
    os.system('clear') 
    to_read = False
    while to_read is False:
        typewriter('''
The heavy door slowly opens as the guard slyly smiles at you. You nod at him and
hastly make your way inside.

Although you know you're safe and will defend yourself if you must, you're happy to
move past him. Something about him...

Your first steps into the cave-room echo throughout it.
The candles looming from the ceiling draw your eyes straight ahead onto an altar on
the opposite end of the room.

You make your way towards it...

Next to a lone candle (how long has it been burning?), a rolled parchment lays idle
on top of the altar.

You pick it up, turn it around and inspect the seal.
It reads:

                             'XXXXXXXX'\n
''')
        read = input('Break the seal and read the parchment? ')
        if read in yes:
            os.system('clear')
            to_read = True
        else:
            os.system('clear') 
            to_read = False


# END OR PLAY AGAIN?
def end_of_game():
    play_again = input('\n>>> Play again? ')
    if play_again in yes:
        os.system('clear')
        return
    elif play_again in no:
        print('\nUntil next time...\n')
    exit()


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
  
  
# MAIN GAME
while True:
    # start game
    guard_convo()
        
    # hangman mini-game
    hangman()
    
    # cave action
    manuscript()
    
    # manuscript
    exec(open("Final_Script.py").read()) # prints the letter I wrote
    
    # cake
    exec(open("Bday_Ascii.py").read()) # prints the artwork
    
    # pause
    time.sleep(2)
    
    # exit or play again?
    end_of_game()
        
        
        
        
        
        
        
        
        
        












