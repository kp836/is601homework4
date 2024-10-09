import sys
from app.commands import Command


class DiscordCommand(Command):
    command_name = "discord"
    
    def execute(self):
        print(f'I WIll send something to discord')
        