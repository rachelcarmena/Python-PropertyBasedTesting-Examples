import pytest
from collection import Collection

from hypothesis import given, settings, Verbosity
from hypothesis.strategies import integers, lists


@settings(verbosity=Verbosity.verbose)
@given(lists(integers()), integers())
def test_that_a_collection_contains_one_more_element_after_insertion(a_list, element):
    assert False

#@settings(verbosity=Verbosity.verbose)
#@given(lists(integers()), integers())
#def test_that_a_collection_contains_the_inserted_element(a_list, element):
#    assert False
#
#@settings(verbosity=Verbosity.verbose)
#@given(lists(integers(min_value=0, max_value=50)), integers(min_value=0, max_value=50))
#def test_that_a_collection_contains_one_element_less_after_deletion(a_list, element):
#    assert False
#
#@settings(verbosity=Verbosity.verbose)
#@given(lists(integers(min_value=0, max_value=50)), integers(min_value=0, max_value=50))
#def test_that_a_collection_does_not_contain_the_removed_element(a_list, element):
#    assert False
#
#@settings(verbosity=Verbosity.verbose)
#@given(lists(integers()), lists(integers()))
#def test_that_two_collections_concatenation_contains_the_elements_of_the_two_collections(a_list, another_list):
#    assert False
#
#@settings(verbosity=Verbosity.verbose)
#@given(lists(integers(min_value=0, max_value=10), min_size=50))
#def test_that_no_duplicated_elements_when_converting_a_collection_to_a_set(a_list):
#    assert False
