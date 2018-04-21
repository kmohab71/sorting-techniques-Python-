from datetime import datetime as dt


class MaxHeap:
    def __init__(self, array):
        self.array = array

    @staticmethod
    def get_left_child(cur):
        return (cur << 1) + 1

    @staticmethod
    def get_right_child(cur):
        return (cur << 1) + 2

    @staticmethod
    def get_parent(cur):
        return (cur - 1) >> 1

    def sort(self):
        start = dt.now()
        self.build_max_heap()
        self.print_heap()
        end = dt.now()
        return (end - start).total_seconds()

    def build_max_heap(self):
        start = dt.now()
        for i in range(0, len(self.array)):
            self.max_heapify(int(i))
        end = dt.now()
        return (end - start).total_seconds()

    def print_heap(self):
        arr = []
        for i in range(len(self.array)):
            arr.append(self.array[0])
            self.array[0] = 0
            self.max_heapify(0)

    def max_heapify(self, cur):
        l = self.get_left_child(cur)
        r = self.get_right_child(cur)
        maximum = cur

        if l < len(self.array) and self.array[maximum] < self.array[l]:
            maximum = l

        if r < len(self.array) and self.array[maximum] < self.array[r]:
            maximum = r

        if maximum != cur:
            self.swap(maximum, cur)
            self.max_heapify(maximum)

    def swap(self, maximum, cur):
        tmp = self.array[maximum]
        self.array[maximum] = self.array[cur]
        self.array[cur] = tmp
