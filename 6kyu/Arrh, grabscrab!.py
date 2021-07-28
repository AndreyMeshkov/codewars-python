# Arrh, grabscrab!
#
# https://www.codewars.com/kata/52b305bec65ea40fe90007a7
#
# Pirates have notorious difficulty with enunciating. They tend to blur all the letters together and scream at people.
#
# At long last, we need a way to unscramble what these pirates are saying.
#
# Write a function that will accept a jumble of letters as well as a dictionary, and output a list of words that the pirate might have meant.
#
# For example:
#
# grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
# Should return ["sport", "ports"].
#
# Return matches in the same order as in the dictionary. Return an empty array if there are no matches.
#
# Good luck!

def grabscrab(word, possible_words):
    sorted_word = "".join(sorted(list(word)))
    result = []
    for possible_word in possible_words:
        if sorted_word == "".join(sorted(list(possible_word))):
            result.append(possible_word)
    return result

# Best practice and clever solution:
#
# def grabscrab(said, possible_words):
#     return [ word for word in possible_words if sorted(word) == sorted(said) ]
