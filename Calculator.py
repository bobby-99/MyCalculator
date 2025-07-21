import math

class Calculator:
    def __init__(self):
        self.history = []

    def log_operation(self, operation_name, numbers, result):
        # for logging calculation history
        logged_numbers = numbers if isinstance(numbers, list) else [numbers]
        self.history.append({
            "Operation": operation_name,
            "Numbers": logged_numbers,
            "Result": result
        })

    def addition(self, *nums):
        if not nums:
            self.log_operation("Add", list(nums), 0)
            return 0
        total = sum(nums)
        self.log_operation("Add", list(nums), total)
        return total

    def subtraction(self, *nums):
        if not nums:
            self.log_operation("Subtract", list(nums), 0)
            return 0
        result = nums[0]
        for num in nums[1:]:
            result -= num
        self.log_operation("Subtract", list(nums), result)
        return result

    def multiply(self, *nums):
        if not nums:
            self.log_operation("Multiply", list(nums), 1)
            return 1  # product of an empty set is always 1 (multiplicative identity)
        total = 1
        for num in nums:
            total *= num
        self.log_operation("Multiply", list(nums), total)
        return total

    def division(self, *nums):
        if not nums:
            self.log_operation("Division", list(nums), 0)
            return 0
        if len(nums) == 1:
            self.log_operation("Division", list(nums), nums[0])
            return nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num == 0:
                error_message = "Nope! Division by 0 is not allowed"
                self.log_operation("Division", list(nums), error_message)
                return error_message
            result /= num
        self.log_operation("Division", list(nums), result)
        return result

    def exponent(self, *nums):
        if not nums:
            self.log_operation("Exponent", list(nums), 0)
            return 0
        if len(nums) == 1:
            self.log_operation("Exponent", list(nums), nums[0])
            return nums[0]

        # Type checking for all numbers in exponent operation
        for num_val in nums:
            if not isinstance(num_val, (int, float)):
                error_message = f"Error: All inputs for exponent must be numbers. Got '{num_val}' of type {type(num_val).__name__}."
                self.log_operation("Exponent", list(nums), error_message)
                return error_message

        # Start with the rightmost number as the initial exponent value
        calculated_exponent_value = nums[-1]

        # Iterate backwards from the second-to-last number to the second number
        for i in range(len(nums) - 2, 0, -1):
            base_for_current_step = nums[i]
            try:
                calculated_exponent_value = base_for_current_step ** calculated_exponent_value
            except OverflowError:
                error_message = f"Error: Intermediate exponent result ({base_for_current_step}^{calculated_exponent_value}) is too large."
                self.log_operation("Exponent", list(nums), error_message)
                return error_message
            except Exception as e: # Catch other potential errors during math
                error_message = f"Error during intermediate exponent calculation: {e}"
                self.log_operation("Exponent", list(nums), error_message)
                return error_message


        # Finally, apply the leftmost base to the accumulated exponent value
        final_base = nums[0]
        try:
            final_result = final_base ** calculated_exponent_value
        except OverflowError:
            error_message = f"Error: Final exponent result ({final_base}^{calculated_exponent_value}) too large."
            self.log_operation("Exponent", list(nums), error_message)
            return error_message
        except Exception as e:
            error_message = f"Error during final exponent calculation: {e}"
            self.log_operation("Exponent", list(nums), error_message)
            return error_message

        self.log_operation("Exponent", list(nums), final_result)
        return final_result

    def modulo(self, *nums):
        if not nums:
            self.log_operation("Modulo", list(nums), 0)
            return 0
        if len(nums) == 1:
            self.log_operation("Modulo", list(nums), nums[0])
            return nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num == 0:
                error_message = "Nope! Modulo by 0 is not allowed"
                self.log_operation("Modulo", list(nums), error_message)
                return error_message
            result %= num
        self.log_operation("Modulo", list(nums), result)
        return result

    def percentage(self, calculation_type, *nums):
        # Numeric input validation for all percentage types
        for num_val in nums:
            if not isinstance(num_val, (int, float)):
                error_message = f"Error: All input values must be numbers. Got '{num_val}' of type {type(num_val).__name__}."
                self.log_operation("Percentage", list(nums), error_message)
                return error_message

        if calculation_type == "part_of_a_whole":
            if len(nums) != 2:
                error_message = "Error: For 'part_of_a_whole', provide exactly two numbers: [part, whole]."
                self.log_operation("Percentage", list(nums), error_message)
                return error_message
            part, whole = nums
            if whole == 0:
                error_message = "Error: 'Whole' cannot be zero when calculating 'part_of_a_whole'."
                self.log_operation("Percentage", list(nums), error_message)
                return error_message
            result = (part / whole) * 100
            self.log_operation("Percentage", list(nums), result)
            return result
        elif calculation_type == "percent_of_number":
            if len(nums) != 2:
                error_message = "Error: For 'percent_of_number', provide exactly two numbers: [percent_value, number]."
                self.log_operation("Percentage", list(nums), error_message)
                return error_message
            percent_value, number = nums
            result = (percent_value / 100) * number
            self.log_operation("Percentage", list(nums), result)
            return result
        elif calculation_type == "change":
            if len(nums) != 2:
                error_message = "Error: For 'change', provide exactly two numbers: [old_value, new_value]."
                self.log_operation("Percentage", list(nums), error_message)
                return error_message
            old_value, new_value = nums
            if old_value == 0:
                error_message = "Error: 'Old value' cannot be zero when calculating 'percentage change'."
                self.log_operation("Percentage", list(nums), error_message)
                return error_message
            result = ((new_value - old_value) / old_value) * 100
            self.log_operation("Percentage", list(nums), result)
            return result
        else:
            # FIX: Handle unknown percentage calculation types
            error_message = f"Error: Unknown percentage calculation type '{calculation_type}'. " \
                            "Supported types are 'part_of_a_whole', 'percent_of_number', 'change'."
            self.log_operation("Percentage", list(nums), error_message)
            return error_message

    def square_root(self, number): # 'number' should be a single scalar, not a list
        # FIX: Added input validation for square root
        if not isinstance(number, (int, float)):
            error_message = f"Error: Input for square root must be a number. Got '{number}' of type {type(number).__name__}."
            self.log_operation("Sqrt", number, error_message)
            return error_message
        if number < 0:
            error_message = "Error: Cannot calculate square root of a negative number."
            self.log_operation("Sqrt", number, error_message)
            return error_message
        result = math.sqrt(number)
        self.log_operation("Sqrt", number, result)
        return result

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []
        print("History Cleared successfully!")

# USER INTERACTIONS - HELPER FUNCTIONS

def get_input_from_users():
    while True:
        numbers_in_string = input("Enter numbers separated by spaces | Ex: 89 45 3 :\n")
        if not numbers_in_string.strip():
            print("No numbers entered. Please try again.")
            continue
        try:
            numbers = [float(s) for s in numbers_in_string.split()]
            return numbers
        except ValueError:
            print("INVALID INPUTS! Try again with different values")

def menu():
    print("=======*=======")
    print("--Select an Operation--")
    print("A : Addition")
    print("B : Subtraction")
    print("C : Multiplication")
    print("D : Division")
    print("E : Exponent")
    print("F : Square Root")
    print("M : Modulo Operation")
    print("P : Percentage")
    print("H : View History")
    print("Z : Clear History")
    print("X : Exit Calci")
    print("=======*=======")

def run_Calculator_App():

    print("Python Multi-number calculator! Have Fun!")

    my_calculator = Calculator()

    while True:
        menu()
        user_option = input("Enter Your Choice of Operation: ").upper()

        if user_option == "X":
            print("Thanks for having a look around!")
            break

        if user_option == "H":
            # FIX: Access history through the class instance
            current_history = my_calculator.get_history()
            if not current_history:
                print("Empty History.")
            else:
                print("=== History===")
                for index, entry in enumerate(current_history):
                    nums_str = ', '.join(map(str, entry['Numbers']))
                    print(f"{index+1}. Operation: {entry['Operation']}, Numbers: [{nums_str}], Result: {entry['Result']}")
                print("===")
            continue

        if user_option == "Z":
            my_calculator.clear_history()
            continue

        if user_option in ['A', 'B', 'C', 'D', 'E', 'F', 'M' ,'P']:
            numbers = []

            if user_option == "F":
                num_str_sq = input("Enter a single number for Square Root: ")
                if not num_str_sq.strip():
                    print("No number entered. Please try again.")
                    continue
                try:
                    numbers = [float(num_str_sq)]
                except ValueError:
                    print("INVALID INPUT! Please enter a valid number.")
                    continue
            else:
                numbers = get_input_from_users()

            if not numbers: # Handles empty list from get_input_from_users
                continue

            cal_result = None

            if user_option == "A":
                cal_result = my_calculator.addition(*numbers)
            elif user_option == "B":
                cal_result = my_calculator.subtraction(*numbers)
            elif user_option == "C":
                cal_result = my_calculator.multiply(*numbers)
            elif user_option == "D":
                div_result = my_calculator.division(*numbers)
                if isinstance(div_result, str) and div_result.startswith("Error"):
                    print(div_result)
                    continue
                cal_result = div_result
            elif user_option == "E":
                exp_result = my_calculator.exponent(*numbers)
                if isinstance(exp_result, str) and exp_result.startswith("Error"):
                    print(exp_result)
                    continue
                cal_result = exp_result
            elif user_option == "F":
                sq_result = my_calculator.square_root(numbers[0])
                if isinstance(sq_result, str) and sq_result.startswith("Error"):
                    print(sq_result)
                    continue
                cal_result = sq_result
            elif user_option == "M":
                mod_result = my_calculator.modulo(*numbers)

                if isinstance(mod_result, str) and mod_result.startswith("Error"):
                    print(mod_result)
                    continue
                cal_result = mod_result
            elif user_option == "P":
                print('''Types of Percentage Operations:
                        1. part_of_a_whole (Eg., if Marks 45 out of 80, calculate percentage)
                        2. percent_of_number (Eg., 20% of 300)
                        3. change (Eg., on 10% increase, another 20% is implied)''')
                percentage_type = input("Type the operation of your choice (Exact string) :")
                per_result = my_calculator.percentage(percentage_type, *numbers)

                if isinstance(per_result, str) and per_result.startswith("Error"):
                    print(per_result)
                    continue
                cal_result = per_result

            # Only print result if calculation wasn't an error message
            if cal_result is not None and not (isinstance(cal_result, str) and cal_result.startswith("Error")):
                print(f'\nResult: {cal_result}\n')
            elif cal_result is None:
                pass

        else:
            print("Please enter correct options from the above provided options")

if __name__ == "__main__":
    run_Calculator_App()