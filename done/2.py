# Задание 2: 1.Написать игру "Виселица на поле чудес" для 
# консоли на 10 баллов ⦁ У вас есть слово, например "олень" 
# ⦁ Необходимо отрисовать для игрока какие-либо символы, 
# например \u25A0 по количеству букв в выбранном слове: 
# ■ ■ ■ ■ ■ ⦁ Необходимо установить счётчик «жизни» в какое-либо 
# значение, пусть будет равно длине слова. ⦁ Предложить игроку 
# ввести букву или всё слово целиком. ⦁ Если буква правильная, 
# то слово из символов перерисовывается с видимой буквой 
# (или буквами). ⦁ Если буква неправильная, то у игрока 
# отнимается одна «жизнь». ⦁ Если игрок ввёл слово и это 
# слово правильно, либо это последняя правильная буква, либо у 
# игрока закончились «жизни», то игра заканчивается.   Условие   
# Вся программа должна состоять из двух частей: основного файла 
# и модуля. В основном файле должна быть описана только логика 
# программы: циклы, условия, вызовы функций. Никаких print, 
# input, арифметических операций и т.п. в этом файле быть не 
# должно. В модуле должны быть описаны все функции.   
# Опишите логику программы используя декомпозицию задачи. 
# За каждое действие должна отвечать своя функция. Помните, 
# что функция должна делать какое-либо одно действие. У вас 
# может получиться нечто такое:   current_word = get_word() 
# table = create_table(current_word) lives = get_lives() while 
# is_alive(lives): show_table(table) answer = prompt('...') if 
# is_word_correct(current_word, answer): show_message('...') 
# break # Дальше в том же духе     Опишите необходимые функции. 
# Например:   def is_alive(lives): return lives > 0 def 
# prompt(msg): return input(msg) def show_message(msg): 
# print(msg) # ...

import module_game2

current_word = module_game2.get_word()
table = module_game2.create_table(current_word)
lives = module_game2.get_lives(current_word)

print(module_game2.show_message(f"Добро пожаловать в Виселицу! Надеюсь мы повеселимся! Угадайте слово: {module_game2.show_table(table)}"))

while module_game2.is_alive(lives):
  answer = module_game2.prompt("Введите букву или слово: ")
  if len(answer) == 1:
    if module_game2.check_letter_in_word(current_word, answer):
      table = module_game2.update_table(table, current_word, answer)
      print(module_game2.show_message(f"Верно! {module_game2.show_table(table)}"))
      if module_game2.game_won(table, current_word):
          print(module_game2.show_message("Поздравляю! Вы победили!"))
          break

    else:
      lives = module_game2.reduce_lives(lives)
      print(module_game2.show_message(f"Неверно. Осталось жизней: {lives}"))
  elif module_game2.is_word_correct(current_word, answer):
    print(module_game2.show_message("Поздравляю! Вы угадали слово!"))
    break
  else:
    lives = module_game2.reduce_lives(lives)
    print(module_game2.show_message(f"Неверно. Осталось жизней: {lives}"))

if not module_game2.is_alive(lives):
  print(module_game2.show_message(f"Вы проиграли. Слово было: {current_word}"))

