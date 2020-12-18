import os
import math
from Calculator import PersistentCalculator

def main():
    calc = PersistentCalculator()

    # Determine drinking age
    age = int(input('How old are you?: '))
    print(f'You are {age} years old?')
    diff = calc.subtract(21, age)
    if diff <= 0:
        if diff == 0:
            at_above = 'at'
        else:
            at_above = 'above'
        print(f'Congrats on being {at_above} the drinking age!')
    else:
        age = abs(diff)
        print(f'Only {age} years til you can drink, legally!')
    print('')

    # Ask about lucky number
    lucky = int(input('Whats your lucky number?: '))
    newLucky = math.trunc(calc.divide(calc.multiply(lucky, 11), 2))
    print(f'New Lucky number: {newLucky}')
    print('')
    
    # Print History
    print('')
    print('History:', calc.history)
    print('')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        pass
