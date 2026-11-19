from batch_calculator import process_calculation
import pytest

@pytest.mark.parametrize("op, a, b", [ ("add", "8.3", "4.21"), ("sub", "15", "2"), ("mul", "3", "5"), ("div", "16", "4"), ("ada", "3", "7"), ("sub", "e", "6"), ("m  ul", " 8", "3  "), ("div", "3", "0"), ("add", "-2", "-4"),])

def test_process_calculation(op, a, b):
	if op == "add":
                if a == "8.3":
                        assert process_calculation(op, a, b) == ("OK", "12", "")
                else:
                        assert process_calculation(op, a, b) == ("OK", "-6", "")
	if op == "sub":
		if a == "15":
			assert process_calculation(op, a, b) == ("OK", "13", "")
		else:
			assert process_calculation(op, a, b) == ("ERROR", "", "INVALID_NUMBER")
	if op == "mul":
		assert process_calculation(op, a, b) == ("OK", "15", "")
	if op == "m  ul":
                assert process_calculation(op, a, b) == ("OK", "24", "")
	if op == "div":
		if a == "16":
			assert process_calculation(op, a, b) == ("OK", "4", "")
		else:
			assert process_calculation(op, a, b) == ("ERROR", "", "DIVISION_BY_ZERO")
	if op == "ada":
		assert process_calculation(op, a, b) == ("ERROR", "", "UNKNOWN_OPERATION")
