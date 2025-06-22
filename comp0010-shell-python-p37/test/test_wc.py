"""
File to test the wc command
"""
import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from parameterized import parameterized
from typing import List

from commands.wccommand import WC
from errors.command_errors import CommandError
from flag import Flag


class TestWC(unittest.TestCase):
    """
    A class to test the WC command
    """

    def setUp(self) -> None:
        self.in_stream = StringIO()
        self.out_stream = StringIO()

    def tearDown(self) -> None:
        self.in_stream.close()
        self.out_stream.close()

    def test_wc_normal(self) -> None:
        """
        Test the wc command in the normal case
        """
        self.in_stream.write("Hello World!")
        self.in_stream.seek(0)
        wc = WC(self.in_stream, self.out_stream, [], [])
        wc.run()
        self.assertEqual(self.out_stream.getvalue(), "1 2 12")

    def test_wc_too_many_flags(self) -> None:
        """
        Test the wc command in the case where the flags are not valid
        """
        flags: List[Flag] = [
            Flag("l", False, "For testing"),
            Flag("w", False, "For testing"),
            Flag("m", False, "For testing"),
        ]
        with self.assertRaises(CommandError):
            WC(self.in_stream, self.out_stream, flags, []).run()

    def test_wc_invalid_flag_name(self) -> None:
        """
        Test the wc command in the case where the flags are not valid
        """
        flags: List[Flag] = [Flag("z", True, "For testing")]
        with self.assertRaises(CommandError):
            WC(self.in_stream, self.out_stream, flags, []).run()

    def test_wc_empty_stream_no_flags(self) -> None:
        """
        Test the wc command with no flags or in stream
        """
        with self.assertRaises(CommandError):
            WC(self.in_stream, self.out_stream, [], []).run()

    @parameterized.expand(
        [
            ("Hello World!", "1 4 7\n", [], ["a b c d"]),
            ("Hello World!", "2 8 16\n", [], ["a b c d\n", "e f g h\n"]),
            ("", "1\n", ["l"], ["a b c d"]),
            ("", "4\n", ["w"], ["a b c d"]),
            ("", "7\n", ["m"], ["a b c d"]),
            ("Hello World!", "1", ["l"], []),
        ]
    )
    def test_valid_wc(self, in_stream, expected_out, flag_names, data) -> None:
        """
        Test the wc command in the case where the flags are valid
        """
        inp = StringIO()
        inp.write(in_stream)
        inp.seek(0)

        flags: List[Flag] = [Flag(n, True, "For testing") for n in flag_names]

        options = [f"file{i}.py" for i, _ in enumerate(data)]
        d = data[0] if data else ""

        with patch("builtins.open", side_effect=mock_open(read_data=d)):
            wc = WC(inp, self.out_stream, flags, options)
            exit_code = wc.run()
            self.assertEqual(self.out_stream.getvalue(), expected_out)
            self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
