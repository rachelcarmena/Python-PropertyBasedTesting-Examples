import pytest
from calculator import Calculator

from hypothesis import given, settings, Verbosity
from hypothesis.strategies import integers


@pytest.fixture
def calculator():
    return Calculator()

#
# This test is limited to a particular case
#
def test_when_adding_one_and_two_then_getting_five(calculator):
    assert False

#
# This test is limited to several particular cases
#
@pytest.mark.parametrize('first_operand, second_operand, expected', [(10, 6, 16), (8, 11, 19), (7, 3, 10)])
def test_when_adding_two_numbers_then_getting_the_total(calculator, first_operand, second_operand, expected):
    assert False

#
# These tests are focused on sum properties
#
#@settings(verbosity=Verbosity.verbose)
#@given(integers())
#def test_that_sum_has_an_identity_value(calculator, first_operand):
#    assert False
#
#@settings(verbosity=Verbosity.verbose)
#@given(integers(), integers())
#def test_that_sum_keeps_the_commutative_property(calculator, first_operand, second_operand):
#    assert False
#
#@settings(verbosity=Verbosity.verbose)
#@given(integers(), integers(), integers())
#def test_that_sum_keeps_the_associative_property(calculator, first_operand, second_operand, third_operand):
#    assert False
