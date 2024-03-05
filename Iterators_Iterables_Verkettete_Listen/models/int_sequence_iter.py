class IntegerSequenceIterator:
    def __init__(self, int_sequence):
        self._int_sequence = int_sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._int_sequence):
            item = self._int_sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

    def __len__(self):
        return len(self._int_sequence)

    def append_to_sequence(self, to_append_value):
        actual_len = self.__len__()
        self._int_sequence.append(to_append_value)
        len_after = self.__len__()

        return actual_len == len_after

