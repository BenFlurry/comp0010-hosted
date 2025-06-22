"""
Imports the base commmand, and implements the interface for the echo command
"""
from commands.base_command import BaseCommand
from commands.command_spec import CommandSpecification
from flag import WildcardFlagSpecification


class Echo(BaseCommand):
    """
    class for the echo command, which implements the BaseCommamnd interface
    """
    COMMAND_SPECIFICATION = \
        CommandSpecification("echo", [WildcardFlagSpecification()],
                             ("[ARG]...",
                              "Prints all of [ARG] into the standrd output"
                              " verbatim"))

    def run(self) -> int:
        """
        see BaseCommand.run()
        """
        self.output.write(' '.join(self.options) + '\n')
        return 0
