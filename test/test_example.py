import pytest

from demo_package_py.main import return_one


def test_return_one():
    assert return_one() == 1
