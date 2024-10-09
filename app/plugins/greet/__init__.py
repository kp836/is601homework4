from app.commands import Command


class GreetCommand(Command):
    command_name = "greet"
    
    def execute(self):
        print("Hello, World!")