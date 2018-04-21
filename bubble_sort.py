from datetime import datetime as dt


class BubbleSort:
    def __init__(self, array):
        self.array = array

    def run(self):
        start_time = dt.now()
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        end_time = dt.now()
        return (end_time - start_time).total_seconds()
