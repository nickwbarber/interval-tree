class IntervalTree:
    def __init__(self,
                 data_list,
                 get_low_function,
                 get_high_function):
        self._sorted_data = sorted(
            data_list,
            key=lambda x: get_low_function(x)
        )
        self._root_index = len(self._sorted_data)//2

        self._root = Node(
            self._sorted_data[self._root_index],
            lambda x: get_low_function(x),
            lambda x: get_high_function(x),
        )

    def get_root(self):
        return self._root

class Node:
    def __init__(self,
                 data,
                 get_low_function,
                 get_high_function):
        self._data = data
        self._get_low_function = get_low_function
        self._get_high_function = get_high_function
        self._low = self._get_low_function(self._data)
        self._high = self._get_high_function(self._data)
        self._left = None
        self._right = None
        self._max = self._high

    def get_data(self):
        return self._data

    def get_low(self):
        return self._get_low_function(self.get_data())

    def get_high(self):
        return self._get_high_function(self.get_data())

    def get_left(self):
        return self._left

    def set_left(self,
                 data):
        self._left = data

    def get_right(self):
        return self._right

    def set_right(self,
                  data):
        self._right = data

    def get_max(self):
        return self._max

    def set_max(self):
        return self._max
