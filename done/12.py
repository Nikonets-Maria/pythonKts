# Задание 12: Простой стековый интерпретатор Преамбула   
# Выражения содержат только целые положительные числа, 
# операторы и круглые скобки.   Допустимые операторы в выражении:
#  +: сложение -: вычитание *: умножение /: деление ^: 
# возведение в степень   Операторы не имеют приоритетов, 
# приоритеты задаются круглыми скобками.  Таким образом, 
# результатом выражения 1+((2+3)*(4*5)) будет 101, а выражения 
# 2+((2*3)/(4^5)) будет 2.   Основное задание   Создайте и 
# опишите класс Interpreter конструктор класса должен принимать 
# код в виде строки метод evaluate единственный публичный метод, 
# который доступен пользователю интерпретатора. Он должен 
# вернуть результат выражения.   Как это должно работать   
# interpreter = Interpreter('1 + ((2 + 3) * (4 * 5))') 
# print(interpreter.evaluate())   101   
# interpreter = Interpreter('10 + ((122 + 3) * (14 * 5))') 
# print(interpreter.evaluate())   8760   Подсказки   
# Начните с выражений, в которых нет пробелов и используются 
# только цифры от 0 до 9, то есть (2+3). Когда ваш интерпретатор 
# будет работать, то добавьте возможность использования пробелов 
# и чисел больше 9, то есть (2 + 123)   Для удобства вычисления, 
# после приёма выражения, окружите его круглыми скобками. 
# То есть выражение 2 * (3 + 4) превратить в (2 * 3 + 4)).   
# Для вычисления выражения вам надо создать два стека: для чисел 
# и операторов. Продвигаясь по коду: при нахождении числа 
# добавляйте его в стек для чисел при нахождении оператора 
# добавляйте его в стек для операторов при нахождении символа ): 
# извлеките последний оператор из стека операторов извлеките два 
# последних числа из стека чисел произведите над числами 
# соответствующую операцию добавьте результат операции в стек 
# для чисел когда символы в коде закончатся, извлеките значение 
# из стека чисел – это и будет результат всего выражения   
# Ваша программа не должна упасть из-за ошибок! В случае ошибок 
# пользователь должен получить соответствующее сообщение, 
# поэтому не забудьте проверить выражение на сбалансированность 
# скобок. 
# Задание Написать простой стековый интерпретатор 
# арифметических выражений
class Interpreter:
    def __init__(self, expression):
        self.expression = '(' + expression.replace(' ', '') + ')'  

    def evaluate(self):
        try:
            numbers = []
            operators = []
            i = 0
            while i < len(self.expression):
                char = self.expression[i]
                if char.isdigit():
                    num = ""
                    while i < len(self.expression) and self.expression[i].isdigit():
                        num += self.expression[i]
                        i += 1
                    numbers.append(int(num))
                    continue  

                if char in ['+', '-', '*', '/', '^']:
                    operators.append(char)
                elif char == '(':
                    pass
                elif char == ')':
                    op = operators.pop()
                    num2 = numbers.pop()
                    num1 = numbers.pop()
                    if op == '+':
                        numbers.append(num1 + num2)
                    elif op == '-':
                        numbers.append(num1 - num2)
                    elif op == '*':
                        numbers.append(num1 * num2)
                    elif op == '/':
                        if num2 == 0:
                            raise ZeroDivisionError("Деление на ноль!")
                        numbers.append(num1 // num2) 
                    elif op == '^':
                        numbers.append(num1 ** num2)
                i += 1

            if len(numbers) != 1 or len(operators) !=0:
              raise ValueError("Некорректное арифметическое выражение")

            return numbers[0]

        except IndexError:
            return "Ошибка: Несбалансированные скобки или некорректное выражение"
        except (ValueError,ZeroDivisionError) as e:
            return str(e)


interpreter = Interpreter('1 + ((2 + 3) * (4 * 5))')
print(interpreter.evaluate()) 

interpreter = Interpreter('10 + ((122 + 3) * (14 * 5))')
print(interpreter.evaluate())  

interpreter = Interpreter('(1 + 2) * 3')
print(interpreter.evaluate())

interpreter = Interpreter('10 / 0')
print(interpreter.evaluate()) 

interpreter = Interpreter('1 + 2 +')
print(interpreter.evaluate()) 

interpreter = Interpreter('(1 + 2')
print(interpreter.evaluate()) 

