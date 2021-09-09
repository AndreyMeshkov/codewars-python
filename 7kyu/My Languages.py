# My Languages
#
# https://www.codewars.com/kata/5b16490986b6d336c900007d
#
# Task
# You are given a dictionary/hash/object containing some languages and your test results in the given languages. Return the list of languages where your test score is at least 60, in descending order of the results.
#
# Note: the scores will always be unique (so no duplicate values)
#
# Examples
# {"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
# {"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
# {"C++": 50, "ASM": 10, "Haskell": 20}     -->  []
# My other katas
# If you enjoyed this kata then please try my other katas! :-)
#
# Translations are welcome!

def my_languages(results):
    sorted_results = sorted(results.items(), key = lambda  item: item[1])[::-1]
    result = []
    for tupl in sorted_results:
        if tupl[1] >= 60:
            result.append(tupl[0])
    return result

# Best practice and clever solution:
#
# def my_languages(results):
#     return sorted((l for l,r in results.items() if r>=60), reverse=True, key=results.get)
