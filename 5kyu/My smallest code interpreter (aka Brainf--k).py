# My smallest code interpreter (aka Brainf**k)
#
# https://www.codewars.com/kata/526156943dfe7ce06200063e/train/python
#
# Inspired from real-world Brainf**k, we want to create an interpreter of that language which will support the following instructions:
#
# > increment the data pointer (to point to the next cell to the right).
# < decrement the data pointer (to point to the next cell to the left).
# + increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
# - decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
# . output the byte at the data pointer.
# , accept one byte of input, storing its value in the byte at the data pointer.
# [ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
# ] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
# The function will take in input...
#
# the program code, a string with the sequence of machine instructions,
# the program input, a string, eventually empty, that will be interpreted as an array of bytes using each character's ASCII code and will be consumed by the , instruction
# ... and will return ...
#
# the output of the interpreted code (always as a string), produced by the . instruction.
# Implementation-specific details for this Kata:
#
# Your memory tape should be large enough - the original implementation had 30,000 cells but a few thousand should suffice for this Kata
# Each cell should hold an unsigned byte with wrapping behavior (i.e. 255 + 1 = 0, 0 - 1 = 255), initialized to 0
# The memory pointer should initially point to a cell in the tape with a sufficient number (e.g. a few thousand or more) of cells to its right. For convenience, you may want to have it point to the leftmost cell initially
# You may assume that the , command will never be invoked when the input stream is exhausted
# Error-handling, e.g. unmatched square brackets and/or memory pointer going past the leftmost cell is not required in this Kata. If you see test cases that require you to perform error-handling then please open an Issue in the Discourse for this Kata (don't forget to state which programming language you are attempting this Kata in).

plusminus_value = {'+': 1, '-': -1}
lessmore_value = {'<': -1, '>': 1}
brc_value = {'[': 1, ']': -1}
brc_pair = {'[': ']', ']': '['}


def brain_luck(code, inputs):
    inputl = list(inputs)
    code_ptr = data_ptr = 0
    data = [0]
    output = ''

    while code_ptr != len(code):
        inst = code[code_ptr]

        if inst == '.':
            output += chr(data[data_ptr])

        if inst == ',':
            data[data_ptr] = ord(inputl.pop(0))

        if inst in lessmore_value:
            data_ptr += lessmore_value[inst]
            if data_ptr == len(data):
                data.append(0)

        if inst in plusminus_value:
            data[data_ptr] += plusminus_value[inst]
            data[data_ptr] %= 256

        if (inst == '[' and data[data_ptr] == 0) or (inst == ']' and data[data_ptr] != 0):
            direction = bracket_counter = brc_value[inst]
            while not (code[code_ptr] == brc_pair[inst] and bracket_counter == 0):
                code_ptr += direction
                if code[code_ptr] in brc_value:
                    bracket_counter += brc_value[code[code_ptr]]

        code_ptr += 1

    return output

# Best practice:
#
# from collections import defaultdict
#
# def brain_luck(code, input):
#     p, i = 0, 0
#     output = []
#     input = iter(input)
#     data = defaultdict(int)
#     while i < len(code):
#         c = code[i]
#         if c == '+': data[p] = (data[p] + 1) % 256
#         elif c == '-': data[p] = (data[p] - 1) % 256
#         elif c == '>': p += 1
#         elif c == '<': p -= 1
#         elif c == '.': output.append(chr(data[p]))
#         elif c == ',': data[p] = ord(next(input))
#         elif c == '[':
#             if not data[p]:
#                 depth = 1
#                 while depth > 0:
#                     i += 1
#                     c = code[i]
#                     if c == '[': depth += 1
#                     elif c== ']': depth -= 1
#         elif c == ']':
#             if data[p]:
#                 depth = 1
#                 while depth > 0:
#                     i -= 1
#                     c = code[i]
#                     if c == ']': depth += 1
#                     elif c == '[': depth -= 1
#         i += 1
#     return ''.join(output)
#
# Clever solution:
#
# def brain_luck(code, input_):
#     vars_ = {'m': [0], 'p': 0, 'i': map(ord, input_), 'ip': 0, 'o': []}
#     py_lines = []
#     indent = 0
#     for c in code:
#         cur_indent = indent
#         if   c == '>': line = 'p += 1; p != len(m) or m.append(0)'
#         elif c == '<': line = 'p -= 1'
#         elif c == '+': line = 'm[p] = (m[p] + 1) % 256'
#         elif c == '-': line = 'm[p] = (m[p] - 1) % 256'
#         elif c == '.': line = 'o.append(m[p])'
#         elif c == ',': line = 'm[p] = i[ip]; ip += 1'
#         elif c == '[': line = 'while m[p]:'; indent += 1
#         elif c == ']': line = ''; indent -= 1
#         py_lines.append('\t' * cur_indent + line)
#     exec('\n'.join(py_lines), vars_)
#     return ''.join(map(chr, vars_['o']))