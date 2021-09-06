# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:03:51 2021

Guessing Game

@author: ameek
"""
import random
low = 0
high = 10
secret_number = random.randint(low,high)
guess_limit = 5
guess_counter = 0
attempt = 1

name = input("Please enter your name: ")
print(f"\nWelcome {name}! You get 5 attempts to guess the number.")
print("\nBest of Luck!\n")

while guess_counter < guess_limit:
    print("I'm thinking of a number between '0' and '10'.")
    guess_attempt = int(input(f"\nPlease enter your guess {attempt}: "))
    attempt += 1
    guess_counter += 1
    if guess_attempt < secret_number:
        print(f"\nSorry {name}! {guess_attempt} is too low")
    elif guess_attempt > secret_number:
        print(f"\nSorry {name}! {guess_attempt} is too high")
    elif guess_attempt == secret_number:
        break

if guess_attempt == secret_number:
    print(f"Congratulations! {guess_attempt} is right guess!")
else:
    print("Sorry! You have exhausted all the attempts. Better luck next time!")