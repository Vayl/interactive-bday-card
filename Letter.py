import sys, time, os

text = '''
Your letter goes here :)\n
'''

os.system('clear')

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        if char != '\n':
            time.sleep(0.08)
        else:
            time.sleep(0.8)
    
typewriter(text)

