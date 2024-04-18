import pytest

from demo_package_py.main import capital_case


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(AttributeError):
        capital_case(9)
