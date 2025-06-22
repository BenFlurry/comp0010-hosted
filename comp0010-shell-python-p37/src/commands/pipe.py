"""
A module implementing a runnable pipe
"""
from io import TextIOBase
from errors import check_arguments
from .runnable import Runnable


# Disabled because this class is intentionally short.
# pylint: disable=too-few-public-methods
class Pipe(Runnable):
    """
    Class for a pipe

    Args:
        left (T): The left command or pipe
        right (T): The right command
    """

    @check_arguments
    def __init__(
        self, left: Runnable, right: Runnable, mid_stream: TextIOBase
    ) -> None:
        self.left: Runnable = left
        self.right: Runnable = right
        self.mid_stream: TextIOBase = mid_stream

    def close(self) -> None:
        """
        Closes all resources used by this pipe. The mid stream is closed twice,
        as it is used by both the left and right commands, however python will
        handle this gracefully.
        """
        self.left.close()
        self.right.close()

    @check_arguments
    def run(self) -> int:
        """
        Runs the pipe

        Returns:
            int: The exit code of the pipe
        """
        self.left.run()
        # Seek to the start of the mid stream
        self.mid_stream.seek(0)
        self.right.run()
        return 0
