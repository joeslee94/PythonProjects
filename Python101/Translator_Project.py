vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in vowel:
            translation += "g"
        else:
            translation += letter
    return translation

phrase = input("Enter in a word: ")
print(translate(phrase))