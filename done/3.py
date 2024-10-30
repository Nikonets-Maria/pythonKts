# Задание 3: 1.Усовершенствовать игру "Виселица на поле чудес" 
# Теперь у вас есть список слов с их описанием, из которого 
# случайным образом выбирается слово для игры.   Теперь игроку 
# надо показать не только символы, но и описание, например: 
# ■ ■ ■ ■ ■ Предмет одежды, который носят на ногах   Предложите 
# игроку после каждого тура сыграть ещё или отказаться
# Пусть игра идёт до тех пор, пока не закончатся слова в 
# списке  
import random

def get_word(word_list):
    if not word_list:
        return None, None  
    word, description = random.choice(word_list)
    return word, description


def create_table(word):
    return ["■"] * len(word)


def update_table(table, word, letter):
    new_table = table[:]
    for i, char in enumerate(word):
        if char == letter:
            new_table[i] = letter
    return new_table


def word_guessed(table, word):
    return "".join(table) == word


def play_again():
  while True:
    answer = input("Хотите сыграть еще? (да/нет): ").lower()
    if answer in ["да", "нет"]:
      return answer == "да"
    else:
      print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")


def game_loop(word_list):
    while word_list:
        word, description = get_word(word_list)
        if word is None:
          break
        table = create_table(word)
        lives = len(word)
        print(f"Описание: {description}")
        print(" ".join(table))

        while lives > 0 and not word_guessed(table, word):
            guess = input("Введите букву: ").lower()
            if guess in word:
                table = update_table(table, word, guess)
                print(" ".join(table))
            else:
                lives -= 1
                print(f"Неправильно! Осталось {lives} попыток.")
            print(" ".join(table))

        if word_guessed(table, word):
            print("Вы угадали!")
        else:
            print(f"Вы проиграли! Слово было: {word}")

        word_list.remove((word, description))
        if not play_again():
          break



word_list = [
    ("кот", "Мурчащее домашнее"),
    ("лук", "овощ который заставит вас плакать"),
    ("питон", "большая змея"),
    ("сон", "то чего не будет в нашей жизни"),
]

game_loop(word_list)
