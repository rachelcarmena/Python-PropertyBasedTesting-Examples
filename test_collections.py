import pytest

from hypothesis import given, settings, Verbosity
from hypothesis.strategies import integers, lists

# Reason of these methods:
# - 'append' and 'remove' methods for a list don't return any value and update the same list
# - Desire to inmutability
def append(a_list, element):
    return a_list + [element]

def remove(a_list, element):
    new_list = a_list[:]
    new_list.remove(element)
    return new_list

@settings(verbosity=Verbosity.verbose)
@given(lists(integers()), integers())
def test_that_a_list_contains_one_more_element_after_insertion(a_list, element):
    assert len(append(a_list, element)) == len(a_list) + 1

@settings(verbosity=Verbosity.verbose)
@given(lists(integers()), integers())
def test_that_a_list_contains_the_inserted_element(a_list, element):
    assert element in append(a_list, element)

@settings(verbosity=Verbosity.verbose)
@given(lists(integers(min_value=0, max_value=50)), integers(min_value=0, max_value=50))
def test_that_a_list_contains_one_element_less_after_deletion(a_list, element):
    new_list = append(a_list, element)
    assert len(remove(new_list, element)) == len(new_list) - 1

@settings(verbosity=Verbosity.verbose)
@given(lists(integers(min_value=0, max_value=50)), integers(min_value=0, max_value=50))
def test_that_a_list_does_not_contain_the_removed_element(a_list, element):
    new_list = append(a_list, element)
    assert remove(new_list, element).count(element) == new_list.count(element) - 1

@settings(verbosity=Verbosity.verbose)
@given(lists(integers()), lists(integers()))
def test_that_two_lists_concatenation_contains_the_elements_of_the_two_list(first_list, second_list):
    new_list = first_list + second_list
    for element in first_list:
        new_list.remove(element)
    for element in second_list:
        new_list.remove(element)
    assert len(new_list) == 0 

@settings(verbosity=Verbosity.verbose)
@given(lists(integers(min_value=0, max_value=10), min_size=50))
def test_that_no_duplicated_elements_when_converting_a_list_to_a_set(a_list):
    a_set = set(a_list)
    new_list = list(a_set)
    assert all([new_list.count(element) == 1 for element in new_list])
