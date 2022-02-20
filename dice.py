from random import randrange

def d3():
    """Simulating rolling a 3 sided die"""
    roll = randrange(1, 4)
    return roll

def d4():
    """Simulating rolling a 4 sided die"""
    roll = randrange(1, 5)
    return roll

def d6(numberOfDice):
    """Simulating rolling 6 sided die"""
    if numberOfDice == 1:
        roll = randrange(1, 7)
        return roll
    elif numberOfDice == 2:
        roll = randrange(2, 13)
        return roll
    elif numberOfDice == 3:
        roll = randrange(3, 19)
        return roll
    else:
        print("You must choose how many dice to roll")

def d8():
    """Simulating rolling an 8 sided die"""
    roll = randrange(1, 9)
    return roll

def d10(numberOfDice):
    """Simulating rolling 10 sided die"""
    if numberOfDice == 1:
        roll = randrange(1, 11)
        return roll
    elif numberOfDice == 2:
        roll = randrange(1, 101)
        return roll

def d12():
    """Simulating rolling a 12 sided die"""
    roll = randrange(1, 13)
    return roll

def d20():
    """Simulating rolling a 20 sided die"""
    roll = randrange(1, 21)
    return roll
