import sys
from app.commands import Command


class MenuCommand(Command):
    command_name = "menu"
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        print("Available commands:")
        for command_name in self.command_handler.commands.keys():
            print(f" - {command_name}")