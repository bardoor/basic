variables = {}


def get_instruction(code_line: str) -> dict:
    instruction = {}

    # Если в строке кода содержится оператор присваивания
    if ":=" in code_line:
        components = code_line.split(" ") # Разделить строку кода по пробелам
        variable_name = components[0]
        value = components[2]
        instruction = {"operation": "assign", "variable_name": variable_name, "value": value}

    return instruction


def execute(code_line: str) -> None:
    instruction = get_instruction(code_line)
    if instruction["operation"] == "assign":
        variable_name = instruction["variable_name"]
        value = instruction["value"]
        variables[variable_name] = value


if __name__ == '__main__':
    print("Вас приветствует консоль! Удивительно, не правда ли? Вводите команды.")
    while True:
        command = input(">>> ")
        execute(command)
        print("Переменные ")
