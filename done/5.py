# Задание 5: Обработка ошибок при работе с файлом 
# 1.Обработать все возможные ошибки при работе с файлом на 10 
# баллов Дан файл с содержимым в формате «на каждой строке число,
# например: 3 12 23 42 Условия корректного файла 
# Число в первой строке (в примере это 3) указывает на общее 
# количество строк в файле (не считая первую) На каждой строке 
# должно быть только число Никакое другое содержимое не 
# допускается Лишние строки не допускаются (пустые могут быть) 
# Задание   Написать программу, которая запрашивает у 
# пользователя имя файла, зачитывает этот файл и считает сумму 
# всех чисел в файле. Набросок вашей программы может выглядеть 
# так: Запрашиваем имя файла у пользователя Вызываем функцию 
# обработки файла Получаем результат функции Что-то делаем с 
# результатом функции   Данный набросок можно преобразовать в 
# код, который может выглядеть примерно так: 
# file_name = input('Введите имя файла: ') 
# data = process(file_name) # функция process 
# возвращает список чисел, например 
# [12, 23, 42] total = sum(data) print(total)   
# Задача   Отследите все возможные ошибки, которые могут 
# произойти в коде. Ваша программа должна работать корректно 
# и не падать ни при каких условиях. Обратите внимание, 
# что именно это и является главной задачей данной практической 
# работы, а не то, что конкретно происходит с результатом чтения 
# файла.

import os

def process_file(file_name):

    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            if not lines:
                return []

            try:
                expected_lines = int(lines[0].strip()) + 1
            except (ValueError, IndexError):
                raise ValueError("Некорректный формат файла: первая строка должна содержать число.")


            if len(lines) != expected_lines:
                raise ValueError("Некорректный формат файла: количество строк не соответствует указанному.")


            numbers = []
            for i, line in enumerate(lines[1:]):
                try:
                    num = int(line.strip())
                    numbers.append(num)
                except ValueError:
                    raise ValueError(f"Некорректный формат файла: строка {i + 2} не содержит целое число.")
            return numbers

    except FileNotFoundError:
        print(f"Ошибка: файл '{file_name}' не найден.")
        return []
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return []


if __name__ == "__main__":
    file_name = input('Введите имя файла: ')
    data = process_file(file_name)
    total = sum(data)
    print(f"Сумма чисел в файле: {total}")
