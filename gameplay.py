from generate_word import GenerateWord
from keyboard import is_pressed
from colorama import Back, Fore, Style
from os import system

class Gameplay(): # play the game
  def __init__(self): 
    self.game_board=''
    if not self.game():
      print("You lose :( better luck next time")
      
  def game(self, attempts:int=6): # loops the 'guess' method 6 times 
    self.word=GenerateWord()
    for i in range(attempts):
      result = self.guess()
    return result
         
  def guess(self): # guess what the word could be
    
    guess=input().lower() # what do you think the word is?
    if len(guess)!=5: # is your word not 5-letters long?
        system('clear') # clear the terminal
        input("Awe Snap!\nPlease input a 5-letter word\nPress enter to continue ")
        system('clear')
        print(self.game_board + Style.RESET_ALL)
        self.guess()
    elif not guess in self.word.words: # is your guess in my 5-letter word dictionary? 
        system('clear') # clear the terminal
        input("Awe Snap!\nWord does not exist\nPress enter to continue ")
        system('clear')
        print(self.game_board + Style.RESET_ALL)
        self.guess()
    else: # if your word is valid? 
      self.game_board += '\n'
      if self.word.value == guess: # if your guess is correct
          self.game_board += f'{Back.GREEN + Fore.LIGHTGREEN_EX}{self.word.value}'
          print(self.game_board + Style.RESET_ALL)
          print("YOU WIN!!")
          return True 
      else: # if your guess is incorrect
        for index, character in enumerate(guess):
          if character == self.word.value[index]: # if the character is in the right place...
              self.game_board += f'{Back.GREEN + Fore.LIGHTGREEN_EX}{character}'            
          elif character in self.word.value: # if the character is in the wrong place but is in the word, parse ↓
              self.game_board += f'{Back.YELLOW + Fore.LIGHTGREEN_EX}{character}'
          else:
            self.game_board += f'{Back.RED}{character}'
        self.game_board += f'{Style.RESET_ALL}'  
        system('clear')
        print(self.game_board + Style.RESET_ALL)
    
print(f"{Back.CYAN}{Fore.BLUE}   WELCOME TO WORDLE   {Style.RESET_ALL}")   
Gameplay() # start the game