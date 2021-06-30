# Srot the inner ctonnet in dsnnieedcg oredr
#
# https://www.codewars.com/kata/5898b4b71d298e51b600014b
#
# #Srot the inner ctnnoet in dsnnieedcg oredr
#
# You have to sort the inner content of every word of a string in descending order.
# The inner content is the content of a word without first and the last char.
#
# Some examples:
#
# "sort the inner content in descending order" -> "srot the inner ctonnet in dsnnieedcg oredr"
# "wait for me" -> "wiat for me"
# "this kata is easy" -> "tihs ktaa is esay"
# The string will never be null and will never be empty.
# It will contain only lowercase-letters and whitespaces.
#
# In C++ the string is always 0-terminated.
#
#
# Have fun coding it and please don't forget to vote and rank this kata! :-)
#
# I have also created other katas. Take a look if you enjoyed this kata!

def sort_the_inner_content(words):
    return " ".join(sort_word(i) for i in words.split())


def sort_word(word):
    if len(word) < 3:
        return word
    else:
        return f"{word[0]}{''.join(sorted(word[1:-1], reverse=True))}{word[-1]}"

# Best practice:
#
#
# def sort_the_inner_content(str):
#     words = str.split()
#     output = []
#
#     for word in words:
#         if len(word) > 2:
#             output.append(
#                 word[0] + ''.join(sorted(word[1:-1], reverse=True)) + word[-1])
#         else:
#             output.append(word)
#
#     return ' '.join(output)

# Clever solution:
#
# def sort_the_inner_content(words):
#     return ' '.join([''.join([a[0]] + sorted(a[1:-1], reverse=True) + [a[-1]]) if len(a) > 2 else a for a in words.split(' ')])
