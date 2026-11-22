
from calculator import add, subtract, multiply, divide

def number_checker(test_val):
    try:
        float(test_val)
        return True
    except:
        return False

def operation_checker(op_check):
    if op_check != "add" and op_check != "sub" and op_check != "mul" and op_check != "div":
        return False
    else:
        return True

def process_calculation(operation, a_text, b_text):
    operation = operation.replace(" ", "")
    a_text = a_text.replace(" ", "")
    b_text = b_text.replace(" ", "")
    status = ""
    error_code = ""
    result = ""

    if operation_checker(operation) == False:
        error_code = "UNKNOWN_OPERATION"
    elif number_checker(a_text) == False or number_checker(b_text) == False:
        error_code = "INVALID_NUMBER"
    elif b_text == "0" and operation == "div":
        error_code = "DIVISION_BY_ZERO"
    
    if error_code == "":
        status = "OK"
        if operation == "add":
            result = float(format(add(float(a_text),float(b_text)), ".3f"))
        elif operation == "mul":
            result = float(format(multiply(float(a_text),float(b_text)), ".3f"))
        elif operation == "sub":
            result = float(format(subtract(float(a_text),float(b_text)), ".3f"))
        elif operation == "div":
            result = float(format(divide(float(a_text),float(b_text)), ".3f"))
    else:
        status = "ERROR"
    
    return(status, result, error_code)
