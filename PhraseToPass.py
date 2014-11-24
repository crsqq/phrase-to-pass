#!/usr/bin/env python3
import re
import sys


def phrase_to_list(p):
    '''
    (string) -> list of strings

    Splits up a given phrase into individual list items, special characters are
    treated as separate items.
    '''
    p = p.lower()
    words = p.split()

    special_characters = '!?,;.:-_'
    parts = []

    for item in words:

        if item[len(item) - 1] in special_characters and len(item) > 1:
            parts.append(item[:len(item) - 1])
            parts.append(item[len(item) - 1])
        else:
            parts.append(item)

    return parts


def pwgen(l):
    '''
    (list if strings) -> string

    Generates the prototype password.
    '''
    password = ''

    for item in l:
        password = password + item[len(item) - 1]
    return password


def to_upper(s):
    '''
    (string) -> string

    Changes every second character to upper case.
    '''
    password = ''
    upper_or_lower = 0

    for ch in s:
        if re.match('[a-zA-Z]', ch) is not None and upper_or_lower % 2 == 0:
            password = password + ch.upper()
        else:
            password = password + ch

        if re.match('[a-zA-Z]', ch):
            upper_or_lower += 1

    return password


def add_numbers(s):
    '''
    (string) -> string

    Appends a numbers at the end of a given string.
    Number is based on the length of that string.
    '''
    num = len(s) * len(s)
    pw = s + str(num)

    return pw


def all_in_one(phrase):
    splitted_phrase = phrase_to_list(phrase)

    password = pwgen(splitted_phrase)
    password = to_upper(password)
    password = add_numbers(password)

    return password


def main():
    if len(sys.argv) > 1:
        phrase = " ".join(sys.argv[1:])
        password = all_in_one(phrase)
        print(password)
    else:
        phrase = input('Please enter your phrase: ')
        password = all_in_one(phrase)

        pwlength = len(password)

        print(password)
        print(pwlength, 'characters')


if __name__ == '__main__':
    main()
#    try:
#        main()
#    except IndexError:
#        print("IndexError! - Something went wrong :(")
