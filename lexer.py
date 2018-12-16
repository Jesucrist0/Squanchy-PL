#-------------------------------------------------------------------------------
# Copyright (C) 2018 Gabriel Rodriguez Canal
# Copyright (C) 2018 Marcos V. Conde
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# Based on:
# https://gist.github.com/eliben/5797351
#-------------------------------------------------------------------------------


import sys
import re
import os
import time
from statistics import mean 


rules = (
    ('stmt', r'\\n\\t|\\n|\\t'),
    ('other',r'\s+|;'),
    ('Name', r'[a-zA-Z_][\w_]*'),
    ('operator', r'(<=|>=|<<|>>|!=|==|<>|::|<-|->|\*\*)|[:=+\-*%/\^<>\(\)&!}{\[\]|,]'),
    ('number', r'(:?\d*\.)?\d+'),
    ('string', r':?\"+[\w\s]+\"'))

regex = re.compile('|'.join(
    "(?P<%s>%s)" % t for t in rules))


class Token():

    def __init__(self, id, value, pos):
        self.id = id
        self.value = value
        self.pos = pos # error handling

    def __repr__(self):
        return "(%s, %s)" % (self.id, self.value)



def lexer (program):

    """Generate instance(Token).See toke_list and debugging comments.
    """

    #token_list = [] #only for debugging

    module = Token("Module", "Module", -1)
    
    yield module
    #token_list.append(module) #only for debugging
    
    i = 0

    def error_handling ():
        # !!! modificar, añadir linea y corregir la cadena de salida
        error_position = i+1
        pointer = program+"\n"+("-"*(i))+"^"
        print (pointer)
        raise SyntaxError("Unexpected character at position %d: `%s`" % (i+1, program[i]))


    for t in regex.finditer(program):
       
        pos = t.start()
        
        if pos > i:
            print ("previa")
            error_handling()

        i = t.end()
        name = t.lastgroup

        if name == "other":
            continue

        elif name == "stmt":
            id = "%s" % name
            token = Token(id, m.group(0), pos)
        else:
            id = "%s" % name
            token = Token(id, t.group(0), pos)
        
        yield token 
        #token_list.append(token) #only for debugging

    if i < len(program):
        print ("post")
        error_handling()

    end = Token("(end)", "(end)", pos+1)
    
    yield end 
    #token_list.append(end) #only for debugging
    #return token_list #only for debugging



def console ():

    """Interactive console for testing. Must change lexer's code, see debugging comments.
    -- commands:
        exit
        clear
    """

    print ("Squanchy PL Lexer Test")
    print ("v1.0\n")
    
    while True:

        expr = input (">> ")
        
        if expr == "exit": exit()
        if expr == "clear": 
            os.system('clear')
            console()
        print (lexer(expr))


if "--console" in sys.argv:
    console()


if "--test" in sys.argv:

    """Benchmark. SQY Lexer vs Python's tokenize module.
    Same code written in SQY and Python: <code.txt> <code_py.txt>
    """
    factor = 1

    #program = open("code.txt").read()
    #program = program.replace("\n","\\n") # !!! mirar si se puede cambiar
    #program = program.replace("\t","\\t")
    program0 = '1+1+1+1+1+1+1+1+1+1+'
    program = program0

    measureSQY = []
    for i in range(factor):
        measureSQY.append([])
        for j in range(1000):
            start = time.time()
            #print (lexer(program)) # real result with:  print(lexer(program))
            lexer(program)
            end = time.time()
            measureSQY[i].append(end-start)
        program *= 10

    measurePY = []
    program = program0
    for i in range(factor):
        measurePY.append([])
        progfile = open("code_py.txt","w")
        progfile.write(program)

        for j in range(1000):
            start = time.time()
            os.system("python -m tokenize code_py.txt")
            end = time.time()
            measurePY[i].append(float(end-start))
        program *= 10

    sqy_time = list(map(lambda x: mean(x), measureSQY))
    py_time = list(map(lambda x: mean(x), measurePY))

    # compare times
    print ("sqy time >>",sqy_time)
    print ("py time >>",py_time)
    print ("how better? =", list(map(lambda x,y: float(x/y), py_time, sqy_time)),"times")
    exit()

if "--input" in sys.argv:
    f = open("code.txt")
    program = f.read()
    f.close()
    print (program,"\n",lexer (program),"\n")


if "--example" in sys.argv:
    expr = "suma (a,b |c) :: c:a+b"
    print (">>",expr,"\n",lexer (expr),"\n")
    expr = "lista <- [1,2,3,4,5,6]"
    print (">>",expr,"\n",lexer (expr),"\n")

    
