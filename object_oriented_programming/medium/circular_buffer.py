class CircularBuffer:
    def __init__(self, length):
        self._length = length
        self._buffer = [None] * length
        self._read_index = 0
        self._write_index = 0

    def _increment(self, index):
         return (index + 1) % self._length

    def put(self, obj):
        if self._read_index == self._write_index \
            and self._buffer[self._read_index] is not None:
            self._read_index = self._increment(self._read_index)
        self._buffer[self._write_index] = obj
        self._write_index = self._increment(self._write_index)

    def get(self):
        return_obj = self._buffer[self._read_index]
        self._buffer[self._read_index] = None
        if return_obj is not None:
            self._read_index = self._increment(self._read_index)
        return return_obj

buffer = CircularBuffer(3)
# print(buffer._buffer, buffer._write_index, buffer._read_index)

print(buffer.get() is None)          # True

buffer.put(1)
# print(buffer._buffer, buffer._write_index, buffer._read_index)

buffer.put(2)
# print(buffer._buffer, buffer._write_index, buffer._read_index)
print(buffer.get() == 1)             # True
# print(buffer._buffer, buffer._write_index, buffer._read_index)



buffer.put(3)
# print(buffer._buffer, buffer._write_index, buffer._read_index)

buffer.put(4)
# print(buffer._buffer, buffer._write_index, buffer._read_index)

print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True