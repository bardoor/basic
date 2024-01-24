variables = {}


def get_instruction(code_line: str) -> dict:
    instruction = {}

    # Если в строке кода содержится оператор присваивания
    if ":=" in code_line:
        # Разрезаем строку кода по пробелам
        # Затем извлекаем из неё имя переменной и значение
        components = code_line.split(" ")
        variable_name = components[0]
        value = components[2]
        instruction = {"operation": "assign", "variable_name": variable_name, "value": value}
    elif code_line[0:3] == "div":
        components = code_line.split(" ")
        variable_name = components[1]
        podelit_na = components[2]
        instruction = {"operation": "div", "variable_name": variable_name, "podelit_na": podelit_na}

    return instruction


def execute(code_line: str) -> None:
    instruction = get_instruction(code_line)

    # Если операция - присваивание
    if instruction["operation"] == "assign":
        # Достаём из массива имя переменной и значение
        variable_name = instruction["variable_name"]
        value = instruction["value"]

        # Обращаемся к глобальному словарю переменных, 
        # записываем по имени переменной соответствующее значение
        variables[variable_name] = value

    elif instruction["operation"] == "div":
        variable_name = instruction["variable_name"]
        podelit_na = instruction["podelit_na"]
        variables[variable_name] = int(variables[variable_name]) // int(podelit_na)


if __name__ == '__main__':
    print("Вас приветствует консоль! Удивительно, не правда ли? Вводите команды.")
    # Бесконечно просим пользователя вводить команды и исполняем их
    while True:
        command = input(">>> ")
        execute(command)
