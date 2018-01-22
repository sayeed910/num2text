
numberMap = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    20: 'twenty',
    30: 'thirty',
}

def convert(number):
    """Converts number to its string representation
    ex: 30 is converted to thirty"""
    text = numberMap[number]
    return text.capitalize()