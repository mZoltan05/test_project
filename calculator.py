class Calculator:
    def solve(self, x:int, y:int, op:str) -> int:
        match op:
            case '+':
                return self.add(x, y)
            case '-':
                return self.subtract(x, y)
            case '/':
                return self.divide(x, y)
            case '*':
                value = 0
                for _ in range(y):
                    value += x
                return value
            case _:
                raise ValueError(f"Invalid operator {op}")
            
    def add(self, x, y) -> int:
        return x + y

    def subtract(self, x, y) -> int:
        return x - y

    def divide(self, x, y) -> int:
        if y == 0:
            raise ValueError("Can't divide by zero!")
        return x / y
