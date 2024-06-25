# Filter the vowels

letters = ['a', 'b', 'c', 'd', 'e', 'o', 'i', 'u', 'j']


def filter_vowel(letters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letters in vowels


filtered_vowels = filter(filter_vowel, letters)
print(list(filtered_vowels))

