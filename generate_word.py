import random

word_file='words.txt'

class GenerateWord:
  words=[]
  with open(word_file) as file:
    for line in file:
        words.append(line.strip())
  
  random.shuffle(words)
  value = words[0].strip()