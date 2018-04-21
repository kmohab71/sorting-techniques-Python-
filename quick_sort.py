from datetime import datetime as dt


class QuickSort:
    def __init__(self, array):
        self.array = array

    def run(self):
        start = dt.now()
        self.quick_sort(0, len(self.array))
        end = dt.now()
        return (end - start).total_seconds()

    def quick_sort(self, start, end):
        if start < end:
            pivot_index = self.partition(start, end)
            self.quick_sort(start, pivot_index - 1)
            self.quick_sort(pivot_index + 1, end)

    def partition(self, start, end):
        pivot = self.array[start]
        i = start
        for j in range(start + 1, end):
            if self.array[j] >= pivot:
                i += 1
                self.array[j], self.array[i] = self.array[i], self.array[j]
        self.array[i], self.array[start] = self.array[start], self.array[i]
        return i
