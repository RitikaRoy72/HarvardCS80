# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 20:16:35 2024

@author: ritik
"""

# Three suspects have been brought in for a murder: Albert, George, And William.
# One of the three suspects is the murderer. The other two are innocent. 
# Innocent suspects always tell the truth. 
# Albert, George, and William all say that they are not the murderer.
# Albert additionally says that "William is the murderer"
# William additionally says that "Albert or George is innocent"

from logic import *

AlbertMurderer = Symbol("Albert is the murderer")
GeorgeMurderer = Symbol("George is the murderer")
WilliamMurderer = Symbol("William is the murderer")

Albert = Symbol("Albert is innocent")
George = Symbol("George is innocent")
William = Symbol("William is innocent")

symbols = [Albert, George, William, AlbertMurderer, GeorgeMurderer, WilliamMurderer]

knowledge = And(
    Biconditional(AlbertMurderer, And(William, George)),
    Biconditional(WilliamMurderer, And(Albert, George)),
    Biconditional(GeorgeMurderer, And(Albert, William)),
    
    Or(And(Albert, Not(AlbertMurderer)), AlbertMurderer),
    Or(And(George, Not(GeorgeMurderer)), GeorgeMurderer),
    Or(And(William, Not(WilliamMurderer)), WilliamMurderer),
    
    Biconditional(Albert, WilliamMurderer),
    
    Biconditional(William, Or(Albert, George))
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(f"    {symbol}")