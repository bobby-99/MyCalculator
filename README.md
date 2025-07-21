Python Multi-Number Calculator

This is a command-line calculator application built in Python, designed to perform arithmetic operations, manage history, and demonstrate robust error handling and Object-Oriented Programming (OOP) principles.
Features

    Basic Arithmetic: Addition, subtraction, multiplication, and division for multiple numbers.

    Advanced Operations: Exponents (power towers) and modulo.

    Percentage Calculations:

        "Part of a whole" as a percentage.

        "Percentage of a number."

        "Percentage change" between two values.

    Square Root: Compute the square root of a single number.

    Calculation History: View and clear a log of all operations and results.

    Interactive Menu: User-friendly command-line interface.

Key Design Principles
Error Handling

Comprehensive error handling ensures a smooth user experience and prevents crashes:

    Invalid Input Types: Detects and rejects non-numeric inputs.

    Division/Modulo by Zero: Prevents and reports errors.

    Negative Square Roots: Catches and reports errors.

    Argument Count Validation: Checks for correct number of arguments per operation.

    Overflow Protection: Includes checks for extremely large numbers in exponentiation.

    Unknown Operation Types: Gracefully handles unsupported calculation types.

Object-Oriented Programming (OOP) Implementation

The application uses OOP for a modular and maintainable design:

    Calculator Class: Encapsulates core logic, holding state (e.g., history) and defining behavior (calculation methods).

    Methods: Each mathematical operation is a method of the Calculator class, organizing code and promoting reusability.

    self Parameter: Allows methods to access instance attributes and call other methods within the class.

    Encapsulation: Internal workings are encapsulated, exposing only necessary functionality.

How to Run

    Save the Code: Save the Python code (e.g., calculator_app.py) to a file.

    Open Terminal/Command Prompt: Navigate to the file's directory.

    Execute: Run the script using a Python interpreter:

    python calculator_app.py

    or, if python refers to Python 2:

    python3 calculator_app.py

    Follow Prompts: The application will present an interactive menu.
