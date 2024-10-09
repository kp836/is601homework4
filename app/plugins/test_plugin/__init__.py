from app.commands import Command

class TestCommand(Command):
    def execute(self, *args):
        print("Test plugin is working!")