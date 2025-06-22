"""
Interface: A base command. Uses the chain of responsibilty + command
architecture
"""
from abc import abstractmethod
from io import StringIO
from typing import Generic, List, TypeVar

from errors import check_arguments
from flag import FlagSpecification, FlagValue, WildcardFlagSpecification

from .command_spec import AbstractCommandSpecification, CommandSpecification
from .runnable import Runnable

T = TypeVar("T", bool, str, int, float, List[str], List[int], List[float])
HELP_TEXT_FORMAT = """
Usage: {:s} {:s}
{:s}

{:s}
"""


class BaseCommand(Runnable, Generic[T]):
    """
    Base class for a command. All common operations to base commands should be
    implemented here.

    Args:
        input (StringIO): Input stream for the command.
        output (StringIO): Output stream for the command.
        flags (List[FlagValue]): List of flags supported by the command.
        options (List[str]): List of options supported by the command.

    Raises:
        DeveloperSkillIssue: If any of the parameters are not supported by
                             the command
    """

    # NOTE: Because of ABC, Python interpreter handles forcing subclasses to
    # implement methods for us. Hence, we don't have to test the functions that
    # are annotated with @abstractmethod; they are commented with nocover for
    # that reason.

    HELP_FLAG = FlagSpecification("h", str, "Displays this help text")
    COMMAND_SPECIFICATION: CommandSpecification = \
        AbstractCommandSpecification()

    @check_arguments
    def __init__(
        self,
        in_stream: StringIO,
        out_stream: StringIO,
        flags: List[FlagValue],
        options: List[str],
    ) -> None:
        """
        Initializes the BaseCommand object with input and output streams.

        Args:
            input (StringIO): Input stream for the command.
            output (StringIO): Output stream for the command.
            flags (List[Flag]): List of flags supported by the command.
            options (List[str]): List of options supported by the command.

        Raises:
            ValueError: If input or output streams are not provided.
        """
        self.input = in_stream
        self.output = out_stream
        self.flags = flags
        self.options = options

    @abstractmethod
    def run(self) -> int:  # pragma: no cover
        """
        Runs the Unix command with the given flags, arguments, and options.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def help(self) -> str:
        """
        Gets the helptext returned to the user whenever they run command --help

        Returns:
            str: The helptext
        """
        spec = self.COMMAND_SPECIFICATION
        command_name = spec.command_name
        option_helptext, command_desc = spec.command_help_text
        flags_helptext = "\n".join(
            [
                f"  -{flag.name}\t{flag.help_text}"
                for flag in spec.flag_specifications
                if not isinstance(flag, WildcardFlagSpecification)
            ]
        )
        return HELP_TEXT_FORMAT.format(
            command_name, option_helptext, command_desc, flags_helptext
        )

    def close(self) -> None:
        """
        Closes all the resources used by this command. If you find yourself
        calling this, consider using the context manager.

        If this is being run from the root, run with command.run_and_close()

        Example:
            with this_command as command:
                command.run()
        """
        self.input.close()
        self.output.close()
