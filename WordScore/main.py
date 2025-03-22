# # MY CODE 
# n = int(input())  # Number of words
# words = input().split()  # List of words
# vowels = "aeiou"
# total_score = 0

# for word in words:
#     count = sum(1 for char in word.lower() if char in vowels)  # Count vowels in the word
#     score = 1 if count % 2 == 1 else 2  # Score logic: Odd = 1, Even = 2
#     total_score += score  # Add score to total

# print(total_score)


# OTHER CODE 
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))