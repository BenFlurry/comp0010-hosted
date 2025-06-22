"""
a unit test to check the auto import
"""
# pylint: disable=too-few-public-methods
import unittest
from typing import List, Type
from unittest.mock import MagicMock, patch

from commands.auto_import import AutoImport
from commands.base_command import BaseCommand
from commands.command_spec import CommandSpecification
from errors.error_dsi import DeveloperSkillIssue


class MockCommand(BaseCommand):
    """
    A class used to mock the command class
    """
    COMMAND_SPECIFICATION = CommandSpecification('mock_command', [], ('', ''))


class MockCommandWithoutName(BaseCommand):
    """
    A class used to mock the command class where the commandname wasnt given
    """


class MockCommandWithoutInheritance:
    """
    A class used to mock the command class where it doesnt inherit BaseCommand
    """
    COMMAND_SPECIFICATION = CommandSpecification('mock_command', [], ('', ''))


class TestGetCommands(unittest.TestCase):
    """
    unit test class for the AutoImport class
    """

    def setUp(self) -> None:
        """
        Instantiate the AutoImport() for all tests
        """
        self.auto_import = AutoImport()

    def test_correctly_imported(self) -> None:
        """
        Checks that all imported classes are not the BaseCommand, and inherit
        from the BaseCommand
        """
        class_objects = self.auto_import.get_command_objects()
        for obj in class_objects:
            self.assertTrue(issubclass(obj, BaseCommand))
            self.assertNotEqual(obj, BaseCommand)

    @patch('glob.glob')
    @patch('builtins.__import__')
    def test_new_command_added(self, mock_import: MagicMock,
                               mock_glob: MagicMock) -> None:
        """
        This test mocks the glob and import, to mock a new file being added,
        ensuring that the file can have the command_name fetched from the
        class

        Arguments:
            mock_import (MagicMock): the mock function
                for the importing of the module
            mock_glob (MagicMock): the mock function for the globbing of the
                files
        """
        # Mock a file structure
        mock_glob.return_value = [
            '/path/to/commands/existing_command.py',
            '/path/to/commands/new_command.py',
            '/path/to/commands/base_command.py'
        ]

        # A mock module to return for each import
        mock_module = MagicMock()
        mock_module.MockCommand = MockCommand
        mock_module.__name__ = 'mock_module'

        # Configure the mock import to return the mock module
        mock_import.return_value = mock_module

        # Make sure to exclude the base_command.py
        command_objects: List[Type[BaseCommand]] = [
            cmd for cmd in
            self.auto_import.get_command_objects()
            if cmd.__name__ != 'BaseCommand']

        command_names = \
            [cmd.COMMAND_SPECIFICATION.command_name for cmd in command_objects]
        # Check that the mock command was the command names list
        self.assertIn('mock_command', command_names)

        # Check that the mock object was created from the MockCommand class
        for cmd in command_objects:
            self.assertIs(cmd, MockCommand)
            self.assertEqual(
                cmd.COMMAND_SPECIFICATION.command_name, 'mock_command')

    @patch('glob.glob')
    @patch('builtins.__import__')
    def test_missing_command_spec(self, mock_import: MagicMock,
                                  mock_glob: MagicMock) -> None:
        """
        This erroneous test checks that if there is no command specification in
        a command file, that an ErrorDSI is thrown

        This should never ever happen clueless (if it does youre a genius)

        Arguments:
            mock_import (MagicMock): the mock function
                for the importing of the module
            mock_glob (MagicMock): the mock function for the globbing of the
                files
        """
        mock_glob.return_value = ['commands/invalid_command.py']
        mock_module = MagicMock()

        mock_module.MockCommandWithoutName = MockCommandWithoutName
        delattr(mock_module.MockCommandWithoutName.__base__,
                'COMMAND_SPECIFICATION')
        mock_import.return_value = mock_module

        with self.assertRaises(DeveloperSkillIssue):
            self.auto_import.get_command_objects()

    @patch('glob.glob')
    @patch('builtins.__import__')
    def test_command_doesnt_inherit_BaseCommand(self, mock_import: MagicMock,
                                                mock_glob: MagicMock) -> None:
        # pylint: disable=invalid-name
        """
        An erroenous test ensuring that an ErrorDSI is thrown when a command
        is written which does not inherit from BaseCommand

        Python should catch this, since you cannot implement a class inheriting
        from BaseCommmand without implementing command_error and run due to
        BaseCommand being an inherited abstract class with defaults

        mock_import (MagicMock): the mock function
                for the importing of the module
            mock_glob (MagicMock): the mock function for the globbing of the
                files
        """
        # Define the fake command files
        mock_glob.return_value = ['commands/non_inheriting_command.py']

        mock_module = MagicMock()

        with self.assertRaises(DeveloperSkillIssue):
            mock_module.MockCommand = MockCommandWithoutInheritance
            mock_import.return_value = mock_module
            self.auto_import.get_command_objects()


if __name__ == "__main__":
    unittest.main()
