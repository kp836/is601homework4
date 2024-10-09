import sys
from app.commands import Command


class ExitCommand(Command):
    command_name = "exit"
    
    def execute(self):
        sys.exit("Exiting...")