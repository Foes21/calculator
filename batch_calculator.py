<<<<<<< HEAD
"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    
    #Return (status, result, error_code) for one calculation.
    #Inputs are strings. Trim whitespace and use the four imported lab functions.
    #Success: ("OK", numeric_result, "").
    #The error_code is empty on success because there is no error to report.
    #Error: ("ERROR", "", error_code).
    #Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    #See the brief for the full contract. You may add small helper functions.
    
    raise NotImplementedError("Complete process_calculation for the coursework")
=======

from calculator import add, subtract, multiply, divide

def number_checker(test_val):
    try:
        float(test_val)
        return True
    except:
        return False

def operation_checker(op_check):
    if op_check != "add" and op_check != "sub" and op_check != "mul" and op_check != "div" and op_check != "subtract" and op_check != "multiply" and op_check != "divide":
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
    elif b_text == "0" and (operation == "div" or operation == "divide"):
        error_code = "DIVISION_BY_ZERO"
    
    if error_code == "":
        status = "OK"
        if operation == "add":
            result = float(format(add(float(a_text),float(b_text)), ".3f"))
        elif operation == "mul" or operation == "multiply":
            result = float(format(multiply(float(a_text),float(b_text)), ".3f"))
        elif operation == "sub" or operation == "subtract":
            result = float(format(subtract(float(a_text),float(b_text)), ".3f"))
        elif operation == "div" or operation == "divide":
            result = float(format(divide(float(a_text),float(b_text)), ".3f"))
    else:
        status = "ERROR"
    
    return(status, result, error_code)
>>>>>>> ad024cff39cb080f1a0676d2fdb7bec61f686e7d
