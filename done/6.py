# Задание 6: Обработка файлов регулярными выражениями 
# 1.Обработать файл регулярными выражениями На железнодорожном 
# вокзале ведётся журналирование рейсов Каждый рейс в файле 
# журнала занимает одну строку в формате: Рейс [номер-поезда] 
# прибыл/отправился из/в [город] в [время]   
# В файле журнала может присутствовать и другая информация.   
# Текущий журнал может выглядеть так:   Рейс 365 прибыл 
# из Сасово в 12:56:30 сообщение получено в 12:57:20 
# Сохранено в базу данных Рейс А123 из Тулы 12:58:02 
# поломался Рейс 452 отправился в Сочи в 13:04:22 
# сообщение получено в 13:11:32 Ошибка записи в базу данных   
# Задание   Необходимо зачитать файл журнала Выбрать 
# необходимую информацию Представить информацию 
# в виде: [время] - Поезд № номер-поезда из/в город   
# Например:   [12:56:30] - Поезд № 365 из Сасово [13:04:22] - 
# Поезд № 452 в Сочи   Записать преобразованную информацию в 
# новый файл

import re

def read_log_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

def extract_flight_info(line):
    match = re.search(r"Рейс\s+(\w+)\s+прибыл|отправился\s+(из|в)\s+([\w\s]+)\s+в\s+(\d{2}:\d{2}:\d{2})", line, re.IGNORECASE)
    if match:
        time, direction, city, train_number = match.groups()
        return (time, train_number, city.strip(), direction)
    else:
        return None


def format_output(info):
    if info:
        time, train_number, city, direction = info
        return f"[{time}] - Поезд № {train_number} {direction} {city}\n"
    else:
        return ""


def write_to_file(filename, formatted_data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(formatted_data)
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


input_filename = "trainsfile6.txt"
output_filename = "formatted_log.txt"

log_lines = read_log_file(input_filename)
formatted_lines = []

for line in log_lines:
    info = extract_flight_info(line)
    formatted_lines.append(format_output(info))

write_to_file(output_filename, formatted_lines)

print(f"Обработанный файл сохранен как '{output_filename}'")

