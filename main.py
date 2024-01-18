def get_instruction(code_line: str) -> dict:
    instruction = {}
    if ":=" in code_line:
        components = code_line.split(" ")
        variable_name = components[0]
        value = components[2]
        instruction = {"operation": "assign", "variable_name": variable_name, "value": value}

    return instruction
