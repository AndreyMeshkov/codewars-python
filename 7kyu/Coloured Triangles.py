# If you finish this kata, you can try Insane Coloured Triangles by Bubbler, which is a much harder version of this one.
#
# A coloured triangle is created from a row of colours, each of which is red, green or blue. Successive rows, each containing one fewer colour than the last, are generated by considering the two touching colours in the previous row. If these colours are identical, the same colour is used in the new row. If they are different, the missing colour is used in the new row. This is continued until the final row, with only a single colour, is generated.
#
# The different possibilities are:
#
# Colour here:        G G        B G        R G        B R
# Becomes colour:      G          R          B          G
# With a bigger example:
#
# R R G B R G B B
#  R B R G B R B
#   G G B R G G
#    G R G B G
#     B B R R
#      B G R
#       R B
#        G
# You will be given the first row of the triangle as a string and its your job to return the final colour which would appear in the bottom row as a string. In the case of the example above, you would the given RRGBRGBB you should return G.
#
# The input string will only contain the uppercase letters R, G, B and there will be at least one letter so you do not have to test for invalid input.
# If you are only given one colour as the input, return that colour.
# Adapted from the 2017 British Informatics Olympiad

def triangle(row):
    if len(row) == 1:
        return row
    new_row = ""
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            new_row += row[i]
        string = "".join(sorted([row[i], row[i + 1]]))
        if string == "BG":
            new_row += "R"
        elif string == "BR":
            new_row += "G"
        elif string == "GR":
            new_row += "B"
    return triangle(new_row)

# Best practice and clever solution:
#
# COLORS = set("RGB")
#
# def triangle(row):
#     while len(row)>1:
#         row = ''.join( a if a==b else (COLORS-{a,b}).pop() for a,b in zip(row, row[1:]))
#     return row
