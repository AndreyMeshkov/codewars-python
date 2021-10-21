# Credit card issuer checking
#
# https://www.codewars.com/kata/5701e43f86306a615c001868
#
# Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.
#
# Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given card number. If the number cannot be matched then the function should return the string Unknown.
#
# | Card Type  | Begins With          | Number Length |
# |------------|----------------------|---------------|
# | AMEX       | 34 or 37             | 15            |
# | Discover   | 6011                 | 16            |
# | Mastercard | 51, 52, 53, 54 or 55 | 16            |
# | VISA       | 4                    | 13 or 16      |
# Examples
# get_issuer(4111111111111111) == "VISA"
# get_issuer(4111111111111) == "VISA"
# get_issuer(4012888888881881) == "VISA"
# get_issuer(378282246310005) == "AMEX"
# get_issuer(6011111111111117) == "Discover"
# get_issuer(5105105105105100) == "Mastercard"
# get_issuer(5105105105105106) == "Mastercard"
# get_issuer(9111111111111111) == "Unknown"

def get_issuer(number):
    string = str(number)
    length = len(string)
    if (string.startswith("34") or string.startswith("37")) and length == 15:
        return "AMEX"
    elif string.startswith("6011") and length == 16:
        return "Discover"
    elif string[0:2] in ("51", "52", "53", "54", "55") and length == 16:
        return "Mastercard"
    elif string[0] == "4" and (length == 13 or length == 16):
        return "VISA"
    else:
        return "Unknown"

# Best practice:
#
# def get_issuer(number):
#     s = str(number)
#     return ("AMEX"       if len(s)==15 and s[:2] in ("34","37") else
#             "Discover"   if len(s)==16 and s.startswith("6011") else
#             "Mastercard" if len(s)==16 and s[0]=="5" and s[1] in "12345" else
#             "VISA"       if len(s) in [13,16] and s[0]=='4' else
#             "Unknown")

# Clever solution:
#
# VENDORS = [
#     # Name         Begins with    Length
#     ['AMEX',       (34, 37),      (15,)],
#     ['Discover',   (6011,),       (16,)],
#     ['Mastercard', range(51, 56), (16,)],
#     ['VISA',       (4,),          (13, 16)],
# ]
#
#
# def get_issuer(number):
#     return next((
#         vendor[0] for vendor in VENDORS
#         if len(str(number)) in vendor[2] and any(str(number).startswith(str(start)) for start in vendor[1])
#    ), 'Unknown')
