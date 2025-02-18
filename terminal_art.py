import random
import time
import os
import sys

# Clear the screen at the start:
os.system('cls || clear')

MESSAGE = input("Enter the password: ")

DELAY = 0.01
CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
UNLOCK_CHAR_PROBABILITY = 0.004
SPACER = ' '

def main():
 
    locked_columns = [False] * len(MESSAGE)

    try:
        while True:
            # Create a random line of characters, same length as MESSAGE:
            columns = [random.choice(CHARS) for _ in range(len(MESSAGE))]

            # Occasionally "unlock" one character (mark a column as matched):
            if random.random() < UNLOCK_CHAR_PROBABILITY:
                while True:
                    # Pick a random position in the message:
                    r = random.randint(0, len(MESSAGE) - 1)
                    if not locked_columns[r]:
                        # Mark that position as matched/locked
                        locked_columns[r] = True
                        break

            # Check if all positions are now locked:
            if all(locked_columns):
                # Once all are locked, we’ve “cracked” the password.
                for _ in range(5):
                    print(SPACER.join(MESSAGE))
                    time.sleep(DELAY)
                print('GG Kid')
                sys.exit()

            # For each locked column, replace the random char with the correct char:
            for i, is_locked in enumerate(locked_columns):
                if is_locked:
                    columns[i] = MESSAGE[i]

            # Print the characters with a spacer:
            print(SPACER.join(columns))
            time.sleep(DELAY)

    except KeyboardInterrupt:
        print('\nPassword Cracker, by Al Sweigart (Modified)')
        sys.exit()

if __name__ == "__main__":
    main()
