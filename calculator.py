class Calculator:
    def calculate(self, num1, num2):
        results = {
            'addition': num1 + num2,
            'subtraction': num1 - num2,
            'multiplication': num1 * num2,
            'division': num1 / num2 if num2 != 0 else 'undefined'
        }
        return results

# Example usage:
calc = Calculator()
result = calc.calculate(10, 5)
print(result)
