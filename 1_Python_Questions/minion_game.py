# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
def minion_game(string):
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0

    # Loop through the string and calculate scores
    for i in range(len(string)):
        substring_start = string[i]
        if substring_start in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

            # Determine the winner
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


# Sample Input
minion_game("BANANA")
