variables = {}


def get_instruction(code_line: str) -> dict:
    instruction = {}
    if ":=" in code_line:
        components = code_line.split(" ")
        variable_name = components[0]
        value = components[2]
        instruction = {"operation": "assign", "variable_name": variable_name, "value": value}

    return instruction


def execute(code_line: str) -> None:
    instruction = get_instruction(code_line)
    if instruction["operation"] == "assign":
        variable_name = instruction["variable_name"]
        value = instruction["value"]
        variables[vatiable_name] = value
