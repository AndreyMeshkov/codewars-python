# Simple assembler interpreter
#
# https://www.codewars.com/kata/58e24788e24ddee28e000053
#
# This is the first part of this kata series. Second part is here.
#
# We want to create a simple interpreter of assembler which will support the following instructions:
#
# mov x y - copies y (either a constant value or the content of a register) into register x
# inc x - increases the content of the register x by one
# dec x - decreases the content of the register x by one
# jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward, y can be a register or a constant), but only if x (a constant or a register) is not zero
# Register names are alphabetical (letters only). Constants are always integers (positive or negative).
#
# Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.
#
# The function will take an input list with the sequence of the program instructions and will execute them. The program ends when there are no more instructions to execute, then it returns a dictionary with the contents of the registers.
#
# Also, every inc/dec/jnz on a register will always be preceeded by a mov on the register first, so you don't need to worry about uninitialized registers.
#
# Example
# simple_assembler(['mov a 5','inc a','dec a','dec a','jnz a -1','inc a'])
#
# ''' visualized:
# mov a 5
# inc a
# dec a
# dec a
# jnz a -1
# inc a
# ''''
# The above code will:
#
# set register a to 5,
# increase its value by 1,
# decrease its value by 2,
# then decrease its value until it is zero (jnz a -1 jumps to the previous instruction if a is not zero)
# and then increase its value by 1, leaving register a at 1
# So, the function should return
#
# {'a': 1}
# This kata is based on the Advent of Code 2016 - day 12

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def parse_instruction(instruction):
    return instruction.split(' ')


class Program:
    def __init__(self, program):
        self.registers = {}
        self.line = 0
        self.program = program
        self.commands = {'mov': self.execute_mov, 'inc': self.execute_inc,
                         'dec': self.execute_dec, 'jnz': self.execute_jnz}

    def execute_mov(self, *params):
        [destination, origin] = params
        if is_number(origin):
            self.registers[destination] = int(float(origin))
        else:
            self.registers[destination] = self.registers[origin]

    def execute_inc(self, *params):
        [register] = params
        self.registers[register] = self.registers[register] + 1

    def execute_dec(self, *params):
        [register] = params
        self.registers[register] = self.registers[register] - 1

    def execute_jnz(self, *params):
        [flag, inc] = params
        if is_number(flag):
            is_zero = int(float(flag)) == 0
        else:
            is_zero = self.registers[flag] == 0
        if not is_zero:
            self.line = self.line + int(float(inc)) - 1

    def execute(self):
        instructions = [parse_instruction(instruction) for instruction in
                        self.program]
        while self.line < len(instructions):
            instruction = instructions[self.line]
            self.commands[instruction[0]](*instruction[1:])
            self.line = self.line + 1
        return self.registers


def simple_assembler(program):
    return Program(program).execute()

# Best practice and clever solution:
#
# def simple_assembler(program):
#     d, i = {}, 0
#     while i < len(program):
#         cmd, r, v = (program[i] + ' 0').split()[:3]
#         if cmd == 'inc': d[r] += 1
#         if cmd == 'dec': d[r] -= 1
#         if cmd == 'mov': d[r] = d[v] if v in d else int(v)
#         if cmd == 'jnz' and (d[r] if r in d else int(r)): i += int(v) - 1
#         i += 1
#     return d
