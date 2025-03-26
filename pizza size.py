#!/usr/bin/env python3


def pizza_area(diametee):
    from math import pi

    return 2 * pi * ((diameter / 2) ** 2)

if __name == '__main__':

    pizza_size = float(input('Enter the pizza size:'))
    pizza_cost = float(input('Enter the pizza price:'))

    this_pizza_area = pizza_area(pizza_size)
    square_inch_cost = pizza_cost / this_pizza_area

    print(f'You are getting {this_pizza_area:.2f} square inches of pizza.')
    print(f'That is £{square_inch_cost:.2f} per square inch of pizza.')