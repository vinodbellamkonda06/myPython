'''
Program to  check provided inputs are plurel or not
'''

import inflection

singular = input("enter a singular word: ")
plural = input("enter a plural word: ")


def is_plurel(singular, plural):

    word = inflection.pluralize(singular)
    print(word)
    if word == plural:
        print( "true")
    else:
        print("false" )


is_plurel(singular,plural)

