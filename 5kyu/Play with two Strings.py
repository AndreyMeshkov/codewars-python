# Play with two Strings
#
# https://www.codewars.com/kata/56c30ad8585d9ab99b000c54
#
# Your task is to Combine two Strings. But consider the rule...
#
# By the way you don't have to check errors or incorrect input values, everything is ok without bad tricks, only two input strings and as result one output string;-)...
#
# And here's the rule:
# Input Strings a and b: For every character in string a swap the casing of every occurrence of the same character in string b. Then do the same casing swap with the inputs reversed. Return a single string consisting of the changed version of a followed by the changed version of b. A char of a is in b regardless if it's in upper or lower case - see the testcases too.
# I think that's all;-)...
#
# Some easy examples:
#
# Input: "abc" and "cde"      => Output: "abCCde"
# Input: "ab" and "aba"       => Output: "aBABA"
# Input: "abab" and "bababa"  => Output: "ABABbababa"
# Once again for the last example - description from KenKamau, see discourse;-):
#
# a) swap the case of characters in string b for every occurrence of that character in string a
# char 'a' occurs twice in string a, so we swap all 'a' in string b twice. This means we start with "bababa" then "bAbAbA" => "bababa"
# char 'b' occurs twice in string a and so string b moves as follows: start with "bababa" then "BaBaBa" => "bababa"
#
# b) then, swap the case of characters in string a for every occurrence in string b
# char 'a' occurs 3 times in string b. So string a swaps cases as follows: start with "abab" then => "AbAb" => "abab" => "AbAb"
# char 'b' occurs 3 times in string b. So string a swaps as follow: start with "AbAb" then => "ABAB" => "AbAb" => "ABAB".
#
# c) merge new strings a and b
# return "ABABbababa"
#
# There are some static tests at the beginning and many random tests if you submit your solution.
#
# Hope you have fun:-)!

def work_on_strings(a, b):
    a_str = "".join([change_letter(i, b) for i in a])
    b_str = "".join([change_letter(i, a) for i in b])
    return a_str + b_str


def change_letter(letter, string):
    if string.lower().count(letter.lower()) % 2 == 0:
        return letter
    else:
        return letter.lower() if letter.isupper() else letter.upper()

# Best practice and clever solution:
#
# def work_on_strings(a, b):
#     new_a = [letter if b.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in a]
#     new_b = [letter if a.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in b]
#     return ''.join(new_a) + ''.join(new_b)
