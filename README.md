# Roll-dice-Game
Dice Rolling Game 

This is a simple dice rolling game where the user is prompted to decide whether they want to roll two dice.
 Breakdown:

1. Imports the `random` module to generate random numbers.
2. Prints a welcome message: `"Welcome to rolling the dice game!!!!"`.
3. Asks the user if they want to roll the dice by entering input (e.g., "yes" or "no").

   The input is converted to lowercase to handle cases where the user types "Yes", "YES", etc.
4. If the user enters `"yes"`:

   The program rolls two dice(generates two random integers between 1 and 6).
   These values are stored in a list called `dice_choices`.
   The list is **converted to a tuple** and printed, e.g., `(5, 2)`.
5. If the user enters `"no"`:

   It prints `"Thanks for playing !!"`.
6. For any other input:

   It prints `"Invalid choice!!"`.

Purpose:

The code simulates rolling two dice and returning the result as a tuple, with input handling and simple validation for user interaction.

