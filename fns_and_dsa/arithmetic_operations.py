# arithmetic_operations.py

params = ["num1", "num2", "operation"]

def perform_operation(num1, num2, operation):
    operation = operation.strip().lower()
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    else:
        return f"Unsupported operation: {operation}"
