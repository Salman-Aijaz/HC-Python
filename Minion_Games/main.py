def minion_game(string):
    s = len(string)
    vowels = 0
    consonants = 0

    for i in range(s):
        if string[i] in "AEIOU":
            vowels += s - i
        else:
            consonants += s - i

    if vowels > consonants:
        print("Kevin", vowels)
    elif consonants > vowels:
        print("Stuart", consonants)
    else:
        print("Draw")

# Input
input_ = "BANANA"
minion_game(input_)
