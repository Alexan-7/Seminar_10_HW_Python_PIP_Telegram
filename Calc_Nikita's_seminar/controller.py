from methods import add, sub, div, mult

def parseable_data(data): # Sem 4, Task_5_add
    '''получение уравнения в виде строки и преобразование в список
    пример: 1+(1+3-2*(2/3)) -> ['1', '+', '(', '1', '+', '3', '-', '2', '*', '(', '2', '/', '3', ')', ')']'''
    math_equation = []
    math_elem = []
    for i in data:
        if i.isdigit(): # Метод isdigit() = True, если все символы в строке являются цифрами, иначе = False
            math_elem.append(i)
        elif (not i.isdigit()) and math_elem:
            math_equation.append(int(''.join(math_elem))) # добавляем в список со знаками и скобками (стр. 6)
            math_equation.append(i)
            math_elem = []
        elif (not i.isdigit()) and (not math_elem):
            math_equation.append(i)
    if math_elem:
        math_equation.append(int(''.join(math_elem)))
    return math_equation # возвращаем список-массив с элементами уравнения

def calculate(part_list):
    '''вычисление примера, полученного в виде списка'''
    result = 0
    if len(part_list) == 1:
        return part_list[0]
    for s in part_list:
        if s == '*' or s == '/':
            # вычисление умножения
            if s == '*':
                index = part_list.index(s)
                result = mult(part_list[index - 1], part_list[index + 1]) # -1 и +1 т.к. по краям от знака
                part_list = part_list[:index - 1] + [result] + part_list[index + 2:]
            # вычисление деления
            else:
                index = part_list.index(s)
                result = div(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + [result] + part_list[index + 2:]

    for s in part_list:
        if s == '+' or s == '-':
            # вычисление сложения
            if s == '+':
                index = part_list.index(s)
                result = add(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + [result] + part_list[index + 2:]
            # вычисление вычитания
            else:
                index = part_list.index(s)
                result = sub(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + [result] + part_list[index + 2:]
    return result

def solution_equation(lst):
    '''раскрытие скобок в примере. Если пример без скобок, то сразу отправляется
    на расчет для получения результата'''
    flag = 1
    while flag == 1:
        if ')' in lst:
            for i in range(lst.index(')'), -1, -1):  # идем по индексам, которые прошли
                if lst[i] == '(':                    # если открывается скобка,...
                    idx = lst.index(')')             # ...то запоминаем индекс закрывающейся
                    elem = calculate(lst[1 + 1:idx]) # считаем то, что находится между скобками
                    lst = lst[:i] + [elem] + lst[idx + 1:]
        elif ')' not in lst:
            flag = 0
    return calculate(lst)