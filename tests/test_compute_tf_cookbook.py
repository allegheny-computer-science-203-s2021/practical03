"""Test cases for the compute_tf_cookbook program"""

from termfrequency import compute_tf_cookbook

# TODO: Add your test cases from the previous practical assignment
#
# TODO: Calculate the coverage of your test suite
#
# TODO: Try to add test cases to increase the coverage of your test suite
#
# TODO: You should try to cover as many regions of the program as is possible
#
# Suggestions:
# -- Study the test coverage report and see what:
#   --> Lines
#   --> Blocks of lines
#   --> Branches
# are currently not being covered by the tests.
# Then, think about how you can create an input that will cause the tests
# to cover those regions of functions in the compute_tf_cookbook program.
#
# -- As you attempt to increase coverage, think carefully about
# how you can run the functions under test in a different way
#
# -- Don't forget that you cannot cover the lines in a function of the
# compute_tf_cookbook if you do not have a test that calls that function!


def test_read_file_populates_data():
    """Checks that the singleline comment count works"""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0


def test_read_file_populates_data_another():
    """Checks that the singleline comment count works"""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) > 0


def test_scan():
    """Checks that the scanning for words works"""
    # pylint: disable=len-as-condition

    assert len(compute_tf_cookbook.words) == 0
    compute_tf_cookbook.scan()
    assert len(compute_tf_cookbook.words) != 0


def test_scan_another():
    """Checks that the scanning for words works"""
    # pylint: disable=len-as-condition

    assert len(compute_tf_cookbook.words) == 0
    compute_tf_cookbook.scan()
    assert len(compute_tf_cookbook.words) == 12


def test_remove_stop_words():
    """Checks that the removal of stop words works"""
    # pylint: disable=len-as-condition

    assert len(compute_tf_cookbook.words) == 12
    compute_tf_cookbook.remove_stop_words()

    assert len(compute_tf_cookbook.words) == 10
