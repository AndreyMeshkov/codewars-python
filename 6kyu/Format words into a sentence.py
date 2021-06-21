# Format words into a sentence
#
# https://www.codewars.com/kata/51689e27fe9a00b126000004
#
# Complete the method so that it formats the words into a single comma separated value. The last word should be separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single formatted string. Empty string values should be ignored. Empty arrays or null/nil values being passed into the method should result in an empty string being returned.
#
# format_words(['ninja', 'samurai', 'ronin']) # should return "ninja, samurai and ronin"
# format_words(['ninja', '', 'ronin']) # should return "ninja and ronin"
# format_words([]) # should return ""

def format_words(words):
    if type(words) == list and len(words) > 0:
        filtered_words = []
        for word in words:
            if type(word) == str and len(word) > 0:
                filtered_words.append(word)

        if len(filtered_words) > 1:
            list_words = filtered_words[0:-1]
            result = ", ".join(list_words) + ' and ' + filtered_words[-1]
            return result
        elif len(filtered_words) == 1:
            return filtered_words[0]
    return ""

# Best practice and clever solution:
#
# def format_words(words):
#     return ', '.join(word for word in words if word)[::-1].replace(',', 'dna ', 1)[::-1] if words else ''
