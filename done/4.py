# Задание 4: Игра "Виселица на поле чудес" (версия 3) 
# 1.Финализируем игру "Виселица на поле чудес" 
# Хорошая идея - хранить список слов с описанием в файле; 
# так его удобнее редактировать: добавлять и удалять слова. 
# Сделайте это!   Вместо "жизней" в виде числа, хорошо бы 
# отрисовывать виселицу по кусочкам, как это происходит в 
# настоящей игре: 
# _____________ |/ | | (_) | \|/ | | | / \ | ____|___   
# Создайте несколько файлов, в каждом из которых хранится 
# фрагмент виселицы. Например в первом файле хранится: 
# _______ |/ | | | | | | | __|________ | |   
# во втором файле хранится: 
# _______ |/ | ( ) | | | | | | __|________ | |   
# и так далее.   После неправильного ответа игрока зачитывайте 
# нужный файл и отрисовывайте его содержимое в консоли.
import random

def load_words(filename):
    """Загружает слова из файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words

def load_picher(stage):
    filename = f'picher{stage+1}.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def display_word(word, guessed_letters):
    displayed = ''.join(letter if letter in guessed_letters else '_' for letter in word)
    return displayed

def play_game():
    words = load_words('words.txt')
    word = random.choice(words).upper()
    guessed_letters = set()
    attempts = 6

    print("Добро пожаловать в игру 'Виселица на поле чудес'!")
    
    while attempts > 0:
        print(load_picher(6 - attempts))  
        print(display_word(word, guessed_letters))
        print(f"Осталось попыток: {attempts}")
        
        guess = input("Введите букву: ").upper()
        
        if guess in guessed_letters:
            print("Вы уже угадали эту букву.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
            print("Неправильно!")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Поздравляем! Вы угадали слово: {word}")
            break
    else:
        print(load_picher(0)) 
        print(f"Вы проиграли! Загаданное слово: {word}")

if __name__ == "__main__":
    play_game()
