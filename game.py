import random
import sys

def main():
    level = get_posint("Level: ")
    computer = random.randint(1, level)
    guess = get_posint("Guess: ")

    while True:
        if guess == computer:
            print("Just right!")
            break
        elif guess < computer:
            print("Too small!")
        else:
            print("Too large!")

        guess = get_posint("Guess: ")


def get_posint(message):
    while True:
        try:
            num = int(input(message))
            if num > 0:
                return num
        except EOFError:
            sys.exit()
        except:
            pass


if __name__ == "__main__":
    main()
