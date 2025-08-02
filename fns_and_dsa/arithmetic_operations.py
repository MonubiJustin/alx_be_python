def perform_operations(num1: float, num2: float, operation: str):
    operations = ["add", "subtract", "multiply", "divide"]
    if operation in operations:
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Zero Division Error"
            return  num1 / num2
    else:
        return "Invalid operator. Please insert either 'add', 'subtract', 'multiply' or 'divide'"
