from mock_command import mock_command
from ft.commands.map import Map


# test cases for Arithmetic operations
def test_map_add3():
    map_test = mock_command(Map)
    map_test.set_input("add", ["3"], ["3", "5"])
    map_test.assert_output(["6", "8"])


def test_map_sub3():
    map_test = mock_command(Map)
    map_test.set_input("sub", ["3"], ["1", "3", "4"])
    map_test.assert_output(["-2", "0", "1"])


def test_map_mul3():
    map_test = mock_command(Map)
    map_test.set_input("mul", ["3"], ["0", "-1", "3"])
    map_test.assert_output(["0", "-3", "9"])


def test_map_id():
    map_test = mock_command(Map)
    map_test.set_input("id", [], ["3", "5"])
    map_test.assert_output(["3", "5"])


def test_map_split_ext():
    map_test = mock_command(Map)
    map_test.set_input("split_ext", [], ["file.txt", "dir/image.jpg"])
    map_test.assert_output(["file\ttxt", "dir/image\tjpg"])


def test_map_format_string():
    map_test = mock_command(Map)
    map_test.set_input("format", ["{:>5}"], ["abc", "b"])
    map_test.assert_output(["  abc", "    b"])


def test_map_format_int():
    map_test = mock_command(Map)
    map_test.set_input("format", ["{:02x}"], ["3", "11", "255"])
    map_test.assert_output(["03", "0b", "ff"])
