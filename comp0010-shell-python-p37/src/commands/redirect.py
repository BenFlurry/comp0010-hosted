"""
The redirect runnable that wraps the inner command.
"""

import shutil
import os
from io import StringIO, TextIOBase
from errors.error_dsi import DeveloperSkillIssue

from .runnable import Runnable


class Redirect(Runnable):
    """
    The redirect runnable. The arguments to this function needs to also be
    linked to the Runnable some way or another.

    Args:
        in_stream (TextIOBase): Input stream to the Redirect object
        out_stream (TextIOBase): Output stream to the Redirect object
        wrapped_in_stream (StringIO): Input stream for the wrapped runnable
        wrapped_out_stream (StringIO): Output stream for the wrapped runnable
        runnable (Runnable): The wrapped runnable object
    """
    def __init__(self,  # pylint: disable=too-many-arguments
                 in_stream: TextIOBase,
                 out_stream: TextIOBase,
                 wrapped_in_stream: StringIO,
                 wrapped_out_stream: StringIO,
                 runnable: Runnable) -> None:
        self.in_stream = in_stream
        self.out_stream = out_stream
        self.wrapped_in_stream = wrapped_in_stream
        self.wrapped_out_stream = wrapped_out_stream
        self.runnable = runnable

    def __streams_are_open_guard(self):
        if self.in_stream.closed or \
           self.out_stream.closed or \
           self.wrapped_in_stream.closed or \
           self.wrapped_out_stream.closed:
            raise DeveloperSkillIssue('one of the streams are closed')

    def stream_is_empty(self, stream: TextIOBase) -> bool:
        """
        If the stream is not seekable, we treat it as non-empty, so we return
        true. Otherwise, checks if the end of the stream > current pos.

        Args:
            stream (TextIOBase): The stream to check the emptiness of

        Returns:
            bool: True if the stream is empty and False otherwise (or if can't
                  tell)
        """
        if not stream.seekable():
            return True

        pos = stream.tell()
        stream.seek(0, os.SEEK_END)
        rtn_val = stream.tell() > pos
        stream.seek(pos, os.SEEK_SET)
        return not rtn_val

    def run(self) -> int:
        """
        Streams the input stream into the wrapped input stream and runs the
        wrapped runnable. Subsequently, streams the runnable output to an
        output stream.

        Raises:
            DeveloperSkillIssue: If any of the streams are closed.
        """
        self.__streams_are_open_guard()

        if not self.stream_is_empty(self.in_stream):
            in_pos = self.wrapped_in_stream.tell()
            shutil.copyfileobj(self.in_stream, self.wrapped_in_stream)
            self.wrapped_in_stream.seek(in_pos)

        with self.runnable:
            out_pos = self.wrapped_out_stream.tell()
            # NOTE: any exception from the runnable will propagate
            rtn_val = self.runnable.run()
            self.wrapped_out_stream.seek(out_pos)
            if not self.stream_is_empty(self.wrapped_out_stream):
                shutil.copyfileobj(self.wrapped_out_stream, self.out_stream)
            return rtn_val

    def close(self):
        self.in_stream.close()
        self.out_stream.close()
        # self.runnable has already been closed in run()
