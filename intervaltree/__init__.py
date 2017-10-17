class IntervalTree:
    def __init__(self,
                 data_list,
                 get_low_function,
                 get_high_function):
        self.sorted_data = sorted(
            data_list,
            key=lambda x: get_low_function(x)
        )
        self.root_index = len(self.sorted_data)//2

        self.root = Node(
            self._sorted_data[self._root_index],
            lambda x: get_low_function(x),
            lambda x: get_high_function(x),
        )

class Node:
    def __init__(self,
                 data,
                 get_low_function,
                 get_high_function):
        self.data = data
        self.get_low_function = get_low_function
        self.get_high_function = get_high_function
        self.low = self._get_low_function(self._data)
        self.high = self._get_high_function(self._data)
        self.max = self._high
        self.left = None
        self.right = None
