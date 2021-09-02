# Salesman's Travel
#
# https://www.codewars.com/kata/56af1a20509ce5b9b000001e/train/python
#
# A traveling salesman has to visit clients. He got each client's address e.g. "432 Main Long Road St. Louisville OH 43071" as a list.
#
# The basic zipcode format usually consists of two capital letters followed by a white space and five digits. The list of clients to visit was given as a string of all addresses, each separated from the others by a comma, e.g. :
#
# "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432".
#
# To ease his travel he wants to group the list by zipcode.
#
# Task
# The function travel will take two parameters r (addresses' list of all clients' as a string) and zipcode and returns a string in the following format:
#
# zipcode:street and town,street and town,.../house number,house number,...
#
# The street numbers must be in the same order as the streets where they belong.
#
# If a given zipcode doesn't exist in the list of clients' addresses return "zipcode:/"
#
# Examples
# r = "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432"
#
# travel(r, "OH 43071") --> "OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432"
#
# travel(r, "NY 56432") --> "NY 56432:High Street Pollocksville/786"
#
# travel(r, "NY 5643") --> "NY 5643:/"
# Note for Elixir:
# In Elixir the empty addresses' input is an empty list, not an empty string.
#
# Note:
# You can see a few addresses and zipcodes in the test cases.

import re


def travel(r, zipcode):
    addresses = r.split(",")
    result = []
    for address in addresses:
        addr = re.search(r"(^\d+) ([a-zA-z.\s]+) ([A-Z]{2} \d+)$", address)
        result.append({
            "house": addr.group(1),
            "street": addr.group(2),
            "zip": addr.group(3)
        })
    streets = []
    houses = []
    for r in result:
        if (r["zip"] == zipcode):
            streets.append(r["street"])
            houses.append(r["house"])
    return "{}:{}/{}".format(
        zipcode,
        ",".join(streets),
        ",".join(houses)
    )

# Best practice and clever solution:
#
# def travel(r, zipcode):
#     streets = []
#     nums = []
#     addresses = r.split(',')
#     for address in addresses:
#         if ' '.join(address.split()[-2:]) == zipcode:
#             streets.append(' '.join(address.split()[1:-2]))
#             nums += address.split()[:1]
#     return '{}:{}/{}'.format(zipcode, ','.join(streets), ','.join(nums))