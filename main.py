import random

import matplotlib.pyplot as plot

from bubble_sort import BubbleSort
from heap import MaxHeap
from quick_sort import QuickSort

data = {"quicksort": [[], []], "bubblesort": [[], []], "heapsort": [[], []]}

MAX = 10000
UNIT = 1000
INPUT_MAX_SIZE = 101

i = 1
while i < INPUT_MAX_SIZE:
    i = i * 10

    # QUICK SORT
    arr = random.sample(range(MAX), i)
    time = QuickSort(arr).run()
    data["quicksort"][0].append(i)
    data["quicksort"][1].append(time * UNIT)

    # BUBBLE SORT
    arr = random.sample(range(MAX), i)
    time = BubbleSort(arr).run()
    data["bubblesort"][0].append(i)
    data["bubblesort"][1].append(time * UNIT)

    # HEAP SORT
    arr = random.sample(range(MAX), i)
    time = MaxHeap(arr).sort()
    data["heapsort"][0].append(i)
    data["heapsort"][1].append(time * UNIT)
plot.plot(data["quicksort"][0], data["quicksort"][1])
plot.plot(data["bubblesort"][0], data["bubblesort"][1])
plot.plot(data["heapsort"][0], data["heapsort"][1])
plot.ylabel("Time in ms")
plot.xlabel("Input size")
plot.legend(["Quick Sort", "Bubble Sort", "Heap Sort"], loc='upper left')
plot.show()
