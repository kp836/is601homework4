import sys
from app.commands import Command

# Class that will take two values to add as parameters
class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Usage: add n n (Example: add 9 2)")
            return
    
        try:
            num1 = float(args[0])
            num2 = float(args[1])
            print(f"Result: {num1 + num2}")
        except ValueError:
            print("Please provide two positive numbers.")