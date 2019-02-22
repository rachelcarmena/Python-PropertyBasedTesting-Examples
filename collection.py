# Notes:
# - 'append' and 'remove' methods for a list don't return any value and update the same list
# - Desire to inmutability
# - There are tuples as a strategy in Hypothesis, but I didn't find an easy option 
#   in that library to create a tuple with a size greater than 1 and different elements.
#   That option is available for lists (min_size).
class Collection:


    def __init__(self, a_list):
        self.a_tuple = tuple(a_list)

    def __len__(self):
        return len(self.a_tuple)

    def __iter__(self): 
        return iter(self.a_tuple)

    def __contains__(self, element):
        return element in self.a_tuple

    def to_set(self):
        a_set = set(self.a_tuple)
        return Collection(tuple(a_set))

    def append(self, element):
        return Collection(self.a_tuple + tuple([element]))

    def remove(self, element):
        new_list = list(self.a_tuple)
        new_list.remove(element)
        return Collection(tuple(new_list))

    def concat(self, another_collection):
        return Collection(self.a_tuple + another_collection.a_tuple)

    def count(self, element):
        return self.a_tuple.count(element)

