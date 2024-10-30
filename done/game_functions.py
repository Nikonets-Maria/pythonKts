import random
import os

def load_word_data(filename):
    # ... (функция загрузки словаря слов и описаний из файла) ...
    # Возвращает список словарей, где каждый словарь - { 'word': 'слово', 'description': 'описание'}
    pass


def get_random_word(word_data):
    # ... (функция случайного выбора слова и описания из списка) ...
    pass


def show_hangman(lives):
    # ... (функция отображения части виселицы в зависимости от количества жизней) ...  читает файлы hangman_part*.txt
    pass


def show_word_and_description(word, guessed_letters, description):
    # ... (функция отображения слова с заменой неотгаданных букв на '_') ...
    pass


def get_player_guess():
    # ... (функция получения ввода от пользователя) ...
    pass


def is_correct_guess(guess, word):
    # ... (функция проверки, является ли догадка правильной) ...
    pass


def is_game_won(word, guessed_letters):
    # ... (функция проверки, выйграл ли игрок) ...
    pass


def show_win_message(word):
    # ... (функция вывода сообщения о выигрыше) ...
    pass


def show_lose_message(word):
    # ... (функция вывода сообщения о проигрыше) ...
    pass


def show_incorrect_guess_message():
    # ... (выводит сообщение о неправильном ответе) ...
    pass


def ask_play_again():
    # ... (спрашивает пользователя, хочет ли он сыграть еще) ...
    pass

