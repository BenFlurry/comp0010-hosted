"""
Package containing the forwarder class.

This is a special runnable that only outputs the loaded string. It is used by
the unsafe decorator when commands encounter __init__ errors.
"""

from io import TextIOBase

from .runnable import Runnable


class Forwarder(Runnable):
    """
    Forwards a string to the standard output.
    Used in the construction of Unsafe.

    Args:
        forwarded_string (str): The string to forward to the output stream
        out_stream (TextIOBase): The target output stream
        ret_val (int): A custom return value returned by run()
    """
    def __init__(self,
                 forwarded_string: str,
                 out_stream: TextIOBase,
                 ret_val: int) -> None:
        self.forwarded_string = forwarded_string
        self.out_stream = out_stream
        self.ret_val = ret_val

    def run(self) -> int:
        self.out_stream.write(self.forwarded_string + '\n')
        return self.ret_val

    def close(self) -> None:
        self.out_stream.close()
