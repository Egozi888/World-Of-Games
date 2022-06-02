# Hey You!!
## WELCOME TO WORLD OF GAMES (V1.01).

This is a python project, that is part of an DevOps Course.
The project lets the user choose between 3 different games:
-  CurrencyRouletteGame.py
- GuessGame_copy.py
- MemoryGame.py

All of the games source code located in the games/ directory

Every time the user wins one of the games, he gets points that saved to txt file 
And can be present in html template using **Flask Library** 

## **The Games:**

### MemoryGame
In this game the server will generate a random list of numbers that will appear for 2 seconds and the disappear.
The user will need to memorized the numbers list and write them down in the terminal
And the difficulty according to the user choice will control the range of the list index numbers, for example:
- Difficulty 1 -will be a list with 5 numbers 
- Difficulty 2 -will be a list with 10 numbers.

### GuessGame
In this game the server will generate a random number that will be kept in the server memory and the user will need to guess the number.
The user will need to guess the number  and write it down in the terminal
And the difficulty according to the user choice will control the range of numbers, for example:
- Difficulty 1 -will be a range of 1-5 numbers 
- Difficulty 2 -will be a range of 1-10 numbers

### CurrencyRouletteGame
In this game the server will generate a random number in dollar currency *using currency API* and the user will need to calculate how much is the number converted to ILS.
And the difficulty according to the user choice will control the how much close or far are you from the right answer, for example:
- Difficulty 1 -will be a range of 10 ILS delta 
- Difficulty 2 -will be a range of 5 ILS delta 

Also every time you win or lose the user will be able *to choose* if hey wants to play another game 
Be sure you **YOU WILL STAY**


**Have Fun Good Luck!!** 

