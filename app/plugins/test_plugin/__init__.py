import logging
from app.commands import Command

class TestCommand(Command):
    def execute(self, *args):
        logging.info("Test plugin is working!")
        print("Test plugin is working!")