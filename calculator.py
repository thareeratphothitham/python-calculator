class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):  # Account for negative numbers
            result = self.add(result, a)
        if b < 0:
            result = -result  # Account for negative multiplier
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = 0
        sign = 1 if (a >= 0 and b >= 0) or (a < 0 and b < 0) else -1  # Account for negative result
        a, b = abs(a), abs(b)  # Work with absolute values for simplicity
        while a >= b:
            a = self.subtract(a, b)
            result = self.add(result, 1)
        return result * sign

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        
        # Ensure we work with absolute values for simplicity
        result = a
        while result >= b or result < 0:
            result = self.subtract(result, b)

        return result

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))