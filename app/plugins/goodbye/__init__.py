from app.commands import Command


class GoodbyeCommand(Command):
    command_name = "goodbye"
    def execute(self):
        print("Goodbye")