import random


def main():
    # colored text
    green = "\033[92m"
    yellow = "\033[93m"
    black = "\033[90m"
    end = "\033[0m"

    # open dictionaries
    game_words = open("game_words.txt").read().split("\n")  # words that show up as chosen words
    guess_words = open("guess_words.txt").read().split("\n")  # words that the player can guess

    # choose random word from game words
    word = game_words[random.randint(0, len(game_words))]

    # attempt loop
    for attempt in range(1, 7):
        # reset variables
        result = ""
        win = None

        # player guess
        print("Attempt", attempt, ":", end=" ")
        guess = input()

        # check if the guessed word is the appropriate length and is a guessable word
        while len(guess) != 5 or guess not in guess_words:
            print("Please try again...")
            print("Attempt", attempt, ":", end=" ")
            guess = input()

        # check if the guessed word matches the chosen word
        for pos in range(0, len(guess)):
            if guess[pos].lower() in word:
                # the character is in the correct position :
                if guess[pos].lower() == word[pos]:
                    result += f"{green}{guess[pos]}{end} "
                    if win is None:
                        win = True
                # the character exists in the chosen word, but is not in the correct position :
                else:
                    result += f"{yellow}{guess[pos]}{end} "
                    win = False
            # the character does not exist in the chosen word :
            else:
                result += f"{black}{guess[pos]}{end} "
                win = False
        if win:
            print("You won!")
            quit()
        print(result)
    print("You lost...")
    print("The word was :", word)


if __name__ == '__main__':
    main()
