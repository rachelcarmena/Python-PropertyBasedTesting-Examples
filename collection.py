# Notes:
# - 'append' and 'remove' methods for a list don't return any value and update the same list
# - Desire to inmutability
class Collection:

    def __init__(self, a_list):
        self.a_list = a_list[:]

    def __len__(self):
        return len(self.a_list)

    def __iter__(self): 
        return iter(self.a_list)

    def __contains__(self, element):
        return element in self.a_list

    def to_set(self):
        a_set = set(self.a_list)
        return Collection(list(a_set))

    def append(self, element):
        return Collection(self.a_list + [element])

    def remove(self, element):
        new_list = self.a_list[:]
        new_list.remove(element)
        return Collection(new_list)

    def concat(self, another_collection):
        return Collection(self.a_list + another_collection.a_list)

    def count(self, element):
        return self.a_list.count(element)

