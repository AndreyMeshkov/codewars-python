# Simple Pig Latin
#
# https://www.codewars.com/kata/520b9d2ad5c005041100000f
#
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    lst = text.split()
    for i in range(len(lst)):
        if lst[i].isalpha():
            lst[i] = f"{lst[i][1:]}{lst[i][0]}ay"
    return " ".join(lst)

# Best practice and clever solution:
#
# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
