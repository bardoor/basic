variables = {}

# input a
# add a 10
# print a

def get_instruction(code_line: str) -> dict:
    instruction = {}

    # Если в строке кода содержится оператор присваивания
    if ":=" in code_line:
        # Разрезаем строку кода по пробелам
        # Затем извлекаем из неё имя переменной и значение
        components = code_line.split(" ")
        variable_name = components[0]
        value = int(components[2])
        instruction = {"operation": "assign", "variable_name": variable_name, "value": value}
    elif 'if' in code_line: 
        components = code_line.split(" ")
        condition = components[1] + components[2] + components[3]
        successful = get_instruction(condition)['result']
        
        if successful == True:
            then_instruction = ""
            for i in range(5, len(components)):
                then_instruction += components[i]
        
        instruction = {'operation': 'if', 'successful': successful,'then_instruction': get_instruction(then_instruction)}

        



    elif "input" in code_line:
        components = code_line.split(" ")
        variable_name = components[1]
        instruction = {"operation": "input","variable_name": variable_name}


    elif code_line[0:3] == "div":
        components = code_line.split(" ")
        variable_name = components[1]
        podelit_na = components[2]
        instruction = {"operation": "div", "variable_name": variable_name, "podelit_na": podelit_na}
    elif code_line[0:3] == "sub":
        components = code_line.split(" ")
        variable_name = components[1]
        minus = components[2]
        instruction = {"operation": "sub", "variable_name": variable_name, "minus": minus}
    elif code_line[0:3] == "add":
        components = code_line.split(" ")
        variable_name = components[1]
        addend = components[2]
        instruction = {"operation": "add", "variable_name": variable_name, "addend": addend}
    elif code_line[0:3] == "mul":
        components = code_line.split(" ")
        variable_name = components[1]
        multi = components[2]
        instruction = {"operation": "mul", "variable_name": variable_name, "multi": multi}
    elif code_line[0:5] == "print":
        components = code_line.split(" ")
        variable_name = components[1]
        instruction = {"operation": "print", "variable_name": variable_name}
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

    elif instruction["operation"] == "input":
        variable_name = instruction["variable_name"]
        variables[variable_name] = int(input("Введите целое число>>"))


    elif instruction["operation"] == "mul":
        variable_name = instruction["variable_name"]
        mul = instruction["multi"]
        variables[variable_name] = int(variables[variable_name]) * int(mul)
    elif instruction["operation"] == "div":
        variable_name = instruction["variable_name"]
        podelit_na = instruction["podelit_na"]
        variables[variable_name] = int(variables[variable_name]) // int(podelit_na)
    elif instruction["operation"] == "add":
        # Достаём из массива имя переменной и значение слагаемого
        variable_name = instruction["variable_name"]
        # Просим у пользователя число >>>
        addend = instruction["addend"]
        # Операция сложения >>> 
        variables[variable_name] = int(variables[variable_name]) + int(addend)
    elif instruction["operation"] == "sub":
        variable_name = instruction["variable_name"]
        minus = instruction["minus"]
        variables[variable_name] = int(variables[variable_name]) - int(minus)
    elif instruction["operation"] == "print":
        variable_name = instruction["variable_name"]
        if variable_name in variables:
            print(variables[variable_name])
        else:
            print(variable_name)

if __name__ == '__main__':
    print("Вас приветствует консоль! Удивительно, не правда ли? Вводите команды.")
    # Бесконечно просим пользователя вводить команды и исполняем их
    while True:
        command = input(">>> ")
        execute(command)