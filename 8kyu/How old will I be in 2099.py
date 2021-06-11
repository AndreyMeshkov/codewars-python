# How old will I be in 2099?
#
# https://www.codewars.com/kata/5761a717780f8950ce001473
#
# Philip's just turned four and he wants to know how old he will be in various years in the future such as 2090 or 3044. His parents can't keep up calculating this so they've begged you to help them out by writing a programme that can answer Philip's endless questions.
#
# Your task is to write a function that takes two parameters: the year of birth and the year to count years in relation to. As Philip is getting more curious every day he may soon want to know how many years it was until he would be born, so your function needs to work with both dates in the future and in the past.
#
# Provide output in this format: For dates in the future: "You are ... year(s) old." For dates in the past: "You will be born in ... year(s)." If the year of birth equals the year requested return: "You were born this very year!"
#
# "..." are to be replaced by the number, followed and proceeded by a single space. Mind that you need to account for both "year" and "years", depending on the result.
#
# Good Luck!

def calculate_age(year_of_birth, current_year):
    if current_year > year_of_birth:
        return f"You are {current_year - year_of_birth} years old." if current_year - year_of_birth > 1 else f"You are 1 year old."
    elif current_year < year_of_birth:
        return f"You will be born in {year_of_birth - current_year} years." if year_of_birth - current_year > 1 else f"You will be born in 1 year."
    elif current_year == year_of_birth:
        return f"You were born this very year!"


# Best practice:
#
# def calculate_age(year_of_birth, current_year):
#     diff = abs(current_year - year_of_birth)
#     plural = '' if diff == 1 else 's'
#     if year_of_birth < current_year:
#         return 'You are {} year{} old.'.format(diff, plural)
#     elif year_of_birth > current_year:
#         return 'You will be born in {} year{}.'.format(diff, plural)
#     return 'You were born this very year!'

# Clever solution:
#
# def calculate_age(birth, curr):
#     diff = abs(curr - birth)
#     age = "%d year%s" % (diff, "s" * bool(diff-1))
#     return "You were born this very year!" if not diff else "You are %s old." % age if curr > birth else "You will be born in %s." % age