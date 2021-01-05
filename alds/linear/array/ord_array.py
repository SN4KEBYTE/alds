# TODO:
# remove duplicates
from bisect import bisect, insort


class OrdArray:
    def __init__(self):
        self.__data = []

    def find(self, value):
        return bisect(self.__data, value)

    def insert(self, value):
        insort(self.__data, value)

    def delete(self, value):
        try:
            i = self.find(value)

            del self.__data[i]
        except ValueError as err:
            raise ValueError from err

    # def get_max(self):
    #     return -1 if len(self.__data) == 0 else self.__data[-1]
    #
    # def remove_max(self):
    #     try:
    #         val = self.__data[-1]
    #
    #         del self.__data[-1]
    #     except IndexError:
    #         val = -1
    #
    #     return val

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, key):
        return self.__data[key]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __contains__(self, item):
        try:
            self.find(item)

            return True
        except ValueError:
            return False

    def __repr__(self):
        return f'OrdArray([{", ".join([str(elem) for elem in self.__data])}])'
