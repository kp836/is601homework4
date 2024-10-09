import sys
from app.commands import Command


class DivideCommand(Command):
    command_name = "divide"
    
    def execute(self, *args):
        if len(args) != 2:
            print("Usage: divide n n (Example: divide 5 2)")
            return
        
        try:
            num1 = float(args[0])
            num2 = float(args[1])

            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            
            print(f"Result: {num1 / num2}")
        except ValueError:
            print("Please provide two valid numbers.")