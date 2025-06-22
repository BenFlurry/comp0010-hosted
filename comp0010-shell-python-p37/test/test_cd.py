"""
Contains unit test for the CD command
"""
import unittest
from io import StringIO
from typing import Callable, List, Type, Optional
from unittest.mock import patch

from commands.cdcommand import CD
from errors.command_errors import (CommandError, ShellFileNotFoundError,
                                   ShellNotADirectoryError)
from errors.error_dsi import DeveloperSkillIssue


class TestCD(unittest.TestCase):
    """
    Tests the CD command class
    """
    def setUp(self):
        self.path = 'some_dir'

    def mock_path_factory(self, accepted_path: str,
                          *,
                          return_value: bool = True,
                          exception: Optional[Type[Exception]] = None
                          ) -> Callable[[str], bool]:
        """
        Builds a function that only accepts one path.

        Args:
            accepted_path (str): The function will attempt to match this
                                 path. If it does not match, an assertion will
                                 be raised.

        Keyword Args:
            return_value (bool): The value to return when the returned function
                                 is called, if the path matches.

            exception (Optional[Type[Exception]]): The function will throw this
                                                   type of exception if the
                                                   path matches.

        Returns:
            Callable[[str], bool]: A function that only accepts one path. If
                                   path does not match, asserts. If path
                                   matches, and exception is not None, that
                                   will be raised if the path matches. Else,
                                   returns true.
        """
        def fn(path: str) -> bool:
            self.assertEqual(path,
                             accepted_path,
                             f'exist not match {path} != {accepted_path}')
            if exception is not None:
                raise exception()
            return return_value
        return fn

    def create_cd_object(self, options: List[str]):
        """
        Creates a good CD object.
        """
        with patch('os.path.exists', self.mock_path_factory(self.path)):
            with patch('os.path.isdir', self.mock_path_factory(self.path)):
                return CD(StringIO(), StringIO(), [], options)

    def test_happy_cd_creation(self):
        """
        This test ensures the happy path for constructing an object passes
        """
        self.create_cd_object([self.path])

    def test_sad_cd_creation_no_options(self):
        """
        If there are no options passed, a CommandError should be raised.
        """
        with self.assertRaisesRegex(CommandError, 'one option'):
            self.create_cd_object([])

    def test_sad_cd_creation_too_many_options(self):
        """
        If there are too many options passed, a CommandError should be raised.
        """
        with self.assertRaisesRegex(CommandError, 'one option'):
            self.create_cd_object(['more', 'than', 'one'])

    def test_sad_cd_creation_no_exist(self):
        """
        If the path doesn't exist, don't continue
        """
        path = 'bad_path'
        with patch('os.path.exists',
                   self.mock_path_factory(path,
                                          return_value=False)):
            with self.assertRaises(ShellFileNotFoundError):
                return CD(StringIO(), StringIO(), [], [path])

    def test_sad_cd_creation_not_dir(self):
        """
        If the path doesn't exist, don't continue
        """
        path = 'bad_path'
        with patch('os.path.exists', self.mock_path_factory(path)):
            with patch('os.path.isdir',
                       self.mock_path_factory(path, return_value=False)):
                with self.assertRaises(ShellNotADirectoryError):
                    return CD(StringIO(), StringIO(), [], [path])

    def test_happy_cd_run(self):
        """
        CD runs happily
        """
        cmd = self.create_cd_object([self.path])
        with patch('os.chdir', self.mock_path_factory(self.path)):
            self.assertEqual(cmd.run(), 0)

    def chdir_run_sad_path_helper(self, chdir_exception: Type[Exception],
                                  expected_exception: Type[Exception],
                                  message: str):
        """
        Format of sad path tests.

        Args:
            chdir_exception (Type[Exception]): The type of exception to be
                                               thrown by os.chdir
            expected_exception (Type[Exception]): The type of exception to
                                                  expect from the run function
            message (str): The error message expected. This will be regexed to
                                                       find a match
        """
        cd = self.create_cd_object([self.path])
        with patch('os.chdir',
                   self.mock_path_factory(self.path,
                                          exception=chdir_exception)):
            with self.assertRaisesRegex(expected_exception, message):
                cd.run()

    def test_directory_deleted_before_command_runs(self):
        """
        If a user is fast enough to delete a directory before the command has a
        chance to run, there should be an error.
        """
        self.chdir_run_sad_path_helper(FileNotFoundError, DeveloperSkillIssue,
                                       'not found')

    def test_directory_not_a_file(self):
        """
        If a user is fast enough to somehow turn a directory into a file before
        the command has a chance to run, there should be an error
        """
        self.chdir_run_sad_path_helper(NotADirectoryError, DeveloperSkillIssue,
                                       'not a dir')

    def test_permissions_error(self):
        """
        If the command doesn't have the permissions to open the file, throw an
        error
        """
        self.chdir_run_sad_path_helper(PermissionError,
                                       CommandError,
                                       'process does not have permission to '
                                       'open the file')

    def test_os_error(self):
        """
        Usually, if this error is thrown, something is very wrong. We just
        blame it on the developers
        """
        self.chdir_run_sad_path_helper(OSError,
                                       DeveloperSkillIssue, 'unknown OSError')


if __name__ == '__main__':
    unittest.main()
