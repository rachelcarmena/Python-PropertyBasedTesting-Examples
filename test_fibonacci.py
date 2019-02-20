import pytest
from fibonacci import fibonacci

from hypothesis import given, settings, Verbosity
from hypothesis.strategies import integers


@settings(verbosity=Verbosity.verbose)
@given(integers(min_value=0, max_value=100))
def test_fibonacci(number):
    assert False

# An alternative for given: 
# @given(integers().filter(lambda x: x >= 0 and x <= 100))
