# Number Guessing Game

A simple number guessing game that runs in the terminal. You pick a range, the computer picks a secret number in it, and you've got 5 tries to find it.

## How it works

1. The game asks for a low and a high number.
2. It picks a random number between them.
3. You get 5 guesses. After each wrong one it tells you whether to go higher or lower.
4. Guess it before you run out and you win. If not, it shows you the number.

A guess outside your range gets you a warning, but it still uses up one of your tries, so be careful.

If you type something that isn't a number, the game just asks again.

## Running it

You only need Python 3, no extra libraries:

    python Guess_Number.py

## Example

    please enter the low number;1
    please enter the high number;50
     you have 5 chance to guess,
     Enter your guess number;25
    its too far, go down :)

## About this project

I wrote this while learning Python, mostly to practice loops, conditions, `try/except` and the `random` module. It's pretty basic, so some ideas for later: a replay option, difficulty levels, or a score counter.