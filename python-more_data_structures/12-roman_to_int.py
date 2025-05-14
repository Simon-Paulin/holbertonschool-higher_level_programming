#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (None)
    roman_value = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_result = 0

    for char in reversed(roman_string):
        value = roman_value.get(char, 0)

        if value < prev_result:
            result -= value
        else: 
            result += value
        
        prev_result = value
    return (result)
