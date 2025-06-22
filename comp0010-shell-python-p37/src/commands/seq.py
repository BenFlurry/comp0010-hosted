"""
module for the seq command
"""

from commands.runnable import Runnable


class Seq(Runnable):
    """
    A class to run the sequence (;) command

    Args:
        left: the left command
        right: the right command
    """

    def __init__(self, left: Runnable, right: Runnable) -> None:
        self.left: Runnable = left
        self.right: Runnable = right

    def run(self) -> int:
        """
        Runs the seq command

        Returns:
            int: exit code of the seq command runner
        """
        self.left.run()
        self.right.run()
        return 0

    def close(self) -> None:
        self.left.close()
        self.right.close()
