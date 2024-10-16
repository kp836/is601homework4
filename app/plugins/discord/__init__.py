import sys
import logging
from app.commands import Command



class DiscordCommand(Command):
    command_name = "discord"
    
    def execute(self):
        logging.info(f'I WIll send something to discord')
        
        print(f'I WIll send something to discord')
        