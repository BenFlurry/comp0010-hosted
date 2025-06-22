"""
The file which implements auto import
"""
import glob
import os.path
import sys
from typing import List
from errors.error_dsi import DeveloperSkillIssue
from commands.base_command import BaseCommand


# pylint: disable=too-few-public-methods
class AutoImport:
    """
    A Class which reads from the commands directory, and returns a list of
    class objects for the shell commands which have been correctly implemented
    """

    def __init__(self):
        """
        Finds the directory of the file, assuming that this file is in the
        commands folder
        """

        self.directory = os.path.dirname(__file__)

        sys.path.append(self.directory)

    def get_command_objects(self) -> List[type]:
        """
        Fetches each command class object and returns as a list of classes
        Returns:
            List[__class__]: a list of class variable for each of the commands
                present in the commands folder
        Raises:
            DeveloperSkillIssue: if a command file does not inherit from
                BaseCommand, or if missing command_name attribute
        """
        command_objects = []

        for file in glob.glob(f'{self.directory}/*command.py'):
            # create a module with the file
            module_name = os.path.basename(file)[:-3]
            # and import it
            if module_name == "base_command":
                continue

            module = __import__(module_name)

            # get the class object for each file
            has_command_name = False
            inherits_base_command = False
            for item_name in dir(module):
                if item_name == "BaseCommand":
                    continue

                item = getattr(module, item_name)
                if isinstance(item, type):
                    if hasattr(item, 'COMMAND_SPECIFICATION'):
                        has_command_name = True
                        if issubclass(item, BaseCommand):
                            inherits_base_command = True
                            command_objects.append(item)

            if not has_command_name:
                raise DeveloperSkillIssue(
                    f"{module_name} doesnt have a command_name"
                )

            if not inherits_base_command:
                raise DeveloperSkillIssue(
                    f"{module_name} doesnt inherit BaseCommand"
                )

        return command_objects
