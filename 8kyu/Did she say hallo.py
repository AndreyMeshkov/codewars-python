# Did she say hallo?
#
# https://www.codewars.com/kata/56a4addbfd4a55694100001f
#
# You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met yesterday evening?
#
# Write a simple regex to check if the string contains the word hallo in different languages.
#
# These are the languages of the possible people you met the night before:
#
# hello - english
# ciao - italian
# salut - french
# hallo - german
# hola - spanish
# ahoj - czech republic
# czesc - polish
# By the way, how cool is the czech republic hallo!!
#
# PS. you can assume the input is a string. PPS. to keep this a beginner exercise you don't need to check if the greeting is a subset of word ('Hallowen' can pass the test)
#
# PS. regex should be case insensitive to pass the tests

def validate_hello(greetings):
    words = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    string = greetings.lower()
    for word in words:
        if string.find(word) > -1:
            return True
    return False

# Best practice and clever solution:
#
# def validate_hello(greetings):
#     return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])
