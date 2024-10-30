def get_word():
  words = ["питон", "жаба", "ясень", "облако", "пощады"]
  import random
  return random.choice(words)


def create_table(word):
  return ["■"] * len(word)


def get_lives(word):
  return len(word)


def is_alive(lives):
  return lives > 0


def show_table(table):
  return "".join(table)


def prompt(msg):
  return input(msg)


def is_word_correct(word, guess):
  return word.lower() == guess.lower()


def update_table(table, word, letter):
  indices = [i for i, char in enumerate(word) if char.lower() == letter.lower()]
  for i in indices:
    table[i] = letter.upper()
  return table


def show_message(msg):
  return msg 


def reduce_lives(lives):
  return lives - 1


def check_letter_in_word(word, letter):
    return letter.lower() in word.lower()

def game_won(table, word):
    return "".join(table).lower() == word.lower()

