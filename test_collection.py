import pytest
from collection import Collection

from hypothesis import given, settings, Verbosity
from hypothesis.strategies import integers, lists


@settings(verbosity=Verbosity.verbose)
@given(lists(integers()), integers())
def test_that_a_list_contains_one_more_element_after_insertion(a_list, element):
    collection = Collection(a_list)

    assert len(collection.append(element)) == len(collection) + 1

@settings(verbosity=Verbosity.verbose)
@given(lists(integers()), integers())
def test_that_a_list_contains_the_inserted_element(a_list, element):
    collection = Collection(a_list)

    assert element in collection.append(element)

@settings(verbosity=Verbosity.verbose)
@given(lists(integers(min_value=0, max_value=50)), integers(min_value=0, max_value=50))
def test_that_a_list_contains_one_element_less_after_deletion(a_list, element):
    collection = Collection(a_list)
    new_collection = collection.append(element)

    assert len(new_collection.remove(element)) == len(new_collection) - 1

@settings(verbosity=Verbosity.verbose)
@given(lists(integers(min_value=0, max_value=50)), integers(min_value=0, max_value=50))
def test_that_a_list_does_not_contain_the_removed_element(a_list, element):
    collection = Collection(a_list)
    new_collection = collection.append(element)

    assert new_collection.remove(element).count(element) == new_collection.count(element) - 1

@settings(verbosity=Verbosity.verbose)
@given(lists(integers()), lists(integers()))
def test_that_two_lists_concatenation_contains_the_elements_of_the_two_list(a_list, another_list):
    collection = Collection(a_list)
    another_collection = Collection(another_list)

    new_collection = collection.concat(another_collection)
    for element in a_list:
        new_collection = new_collection.remove(element)
    for element in another_list:
        new_collection = new_collection.remove(element)
    assert len(new_collection) == 0 

@settings(verbosity=Verbosity.verbose)
@given(lists(integers(min_value=0, max_value=10), min_size=50))
def test_that_no_duplicated_elements_when_converting_a_list_to_a_set(a_list):
    collection = Collection(a_list)

    a_set = collection.to_set()
    assert all([a_set.count(element) == 1 for element in a_set])
