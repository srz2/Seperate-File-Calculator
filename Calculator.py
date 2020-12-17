# This file contains some helpful math functions
# Created: 2020/12/17
# 

def add(x: int, y: int):
    valX = int(x)
    valY = int(y)
    return valX + valY


def sub(x: int, y: int):
    valX = int(x)
    valY = int(y)
    return valX - valY


def div(x: int, y: int):
    valX = int(x)
    valY = int(y)
    return valX / valY


def mul(x: int, y: int):
    valX = int(x)
    valY = int(y)
    return valX * valY

class PersistantCalculator:
    ''' A calculator to keep track of arithmetic calculations'''

    def __init__(self):
        # Create a list in the class to keep track of calculations
        self.history = []

    def add(self, x: int, y: int):
        ''' Add two numbers together (tracked) '''
        self.history.append(f'Adding {x} and {y}')
        return add(x, y)

    def subtract(self, x: int, y: int):
        ''' Subtract two numbers from each other (tracked) '''
        self.history.append(f'Subtraction {x} and {y}')
        return sub(x, y)

    def divide(self, x: int, y: int):
        ''' Divide two numbers (tracked) '''
        self.history.append(f'Dividing {x} and {y}')
        return div(x, y)

    def multiply(self, x: int, y: int):
        ''' Multiply two numbers together (tracked) '''
        self.history.append(f'Multiplying {x} and {y}')
        return mul(x, y)
