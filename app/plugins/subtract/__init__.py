import sys
from app.commands import Command


class SubtractCommand(Command):
    command_name = "subtract"
    
    def execute(self, *args):
        if len(args) != 2:
            print("Usage: subtract n n (Example: subtract 10 3)")
            return
        
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            print(f"Result: {num1 - num2}")
        except ValueError:
            print("Please provide two valid numbers.")
        