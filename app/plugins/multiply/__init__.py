import sys
from app.commands import Command


class MultiplyCommand(Command):
    command_name = "multiply"
    
    def execute(self, *args):
        if len(args) != 2:
            print("Usage: multiply n n (Example: multiply 3 6)")
            return
        
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            print(f"Result: {num1 * num2}")
        except ValueError:
            print("Please provide two valid numbers.")