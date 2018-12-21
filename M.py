import random, time, heapq
import matplotlib.pyplot as plt


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class MinMaxbinarytree(object):
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if (val < node.v):
            if (node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if (node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def get_min(self):
        current = self.root

        # loop down to find the lefmost leaf
        while (current.l is not None):
            current = current.l

        return current.v

    def get_max(self):
        current = self.root

        # loop down to find the lefmost leaf
        while (current.r is not None):
            current = current.r

        return current.v

class MinMaxquicksort(object):
    def __init__(self):
        self.content = []

    def add(self, value):
        self.content.append(value)
        quickSort(self.content, 0 , len(self.content)-1)

    def get_min(self):
        return self.content[0]

    def get_max(self):
        return self.content[-1]


class MinMaxHeap(object):

    def __init__(self):
        self.content_min = []
        self.content_max = []
        # heapq.heapify(self.content_min)
        # heapq.heapify(self.content_max)

    def add(self, value):
        heapq.heappush(self.content_min, value)
        heapq.heappush(self.content_max, -value)

    def get_min(self):
        if len(self.content_min) > 0:
            return self.content_min[0]

    def get_max(self):
        if len(self.content_max) > 0:
            return -self.content_max[0]


class MinMaxBubble(object):

    def __init__(self):
        self.content = []

    def bubble_sort(self):
        for passnum in range(len(self.content) - 1, 0, -1):
            for i in range(passnum):
                if self.content[i] > self.content[i + 1]:
                    temp = self.content[i]
                    self.content[i] = self.content[i + 1]
                    self.content[i + 1] = temp

    def add(self, value):
        self.content.append(value)
        self.bubble_sort()

    def get_min(self):
        return self.content[0]

    def get_max(self):
        return self.content[-1]


def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max


if __name__ == '__main__':
    repetitions = 3
    max_operations = 1000
    step = 200

    values_quicksort_add, values_quicksort_min, values_quicksort_max = [], [], []
    values_binarytree_add, values_binarytree_min, values_binarytree_max = [], [], []
    values_heap_add, values_heap_min, values_heap_max = [], [], []
    values_bubble_add, values_bubble_min, values_bubble_max = [], [], []

    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 1000))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxquicksort()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_quicksort_add.append(tot_time_add )
        values_quicksort_min.append(tot_time_min )
        values_quicksort_max.append(tot_time_max )

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxbinarytree()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_binarytree_add.append(tot_time_add )
        values_binarytree_min.append(tot_time_min )
        values_binarytree_max.append(tot_time_max )

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(5):
            a = MinMaxHeap()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5

        values_heap_add.append(tot_time_add )
        values_heap_min.append(tot_time_min )
        values_heap_max.append(tot_time_max )

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxBubble()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_bubble_add.append(tot_time_add )
        values_bubble_min.append(tot_time_min )
        values_bubble_max.append(tot_time_max )

    print(values_bubble_add)
    print(values_bubble_min)
    print(values_bubble_max)

    print(values_heap_add)
    print(values_heap_min)
    print(values_heap_max)

    print(values_quicksort_add)
    print(values_quicksort_min)
    print(values_quicksort_max)

    print(values_binarytree_add)
    print(values_binarytree_min)
    print(values_binarytree_max)
    xlabels = range(step, max_operations, step)

    plt.plot(xlabels, values_binarytree_add, label='Add')
    plt.plot(xlabels, values_bubble_min, label='Get Min')
    plt.plot(xlabels, values_binarytree_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of binarytree's Solution")
    plt.show()

    plt.plot(xlabels, values_quicksort_add, label='Add')
    plt.plot(xlabels, values_quicksort_min, label='Get Min')
    plt.plot(xlabels, values_quicksort_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of quicksorts's Solution")
    plt.show()

    plt.plot(xlabels, values_heap_add, label='Add')
    plt.plot(xlabels, values_heap_min, label='Get Min')
    plt.plot(xlabels, values_heap_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Heap Solution")
    plt.show()

    plt.plot(xlabels, values_bubble_add, color='b', linestyle='-', label='Add')
    plt.plot(xlabels, values_bubble_min, color='b', linestyle='--', label='Get Min')
    plt.plot(xlabels, values_bubble_max, color='b', linestyle='-.', label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Bubble Sort")
    plt.show()

    plt.plot(xlabels, values_binarytree_add, color='g', linestyle='-', label='binarytree Add')
    plt.plot(xlabels, values_quicksort_add, color='r', linestyle='-', label='quicksort Add')
    plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
    plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Heap Add')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Add")
    plt.show()

    plt.plot(xlabels, values_binarytree_min, color='g', linestyle='--', label='binarytree Get Min')
    plt.plot(xlabels, values_quicksort_min, color='r', linestyle='--', label='quicksort Get Min')
    plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min')
    plt.plot(xlabels, values_bubble_min, color='y', linestyle='--', label='Heap Get Min')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Min")
    plt.show()

    plt.plot(xlabels, values_binarytree_max, color='g', linestyle='-.', label='binarytree Get Max')
    plt.plot(xlabels, values_quicksort_max, color='r', linestyle='-.', label='quicksort Get Max')
    plt.plot(xlabels, values_heap_max, color='b', linestyle='-.', label='Heap Get Max')
    plt.plot(xlabels, values_bubble_max, color='y', linestyle='-.', label='Heap Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Max")
    plt.show()

    plt.plot(xlabels, values_binarytree_add, color='g', linestyle='-', label='binarytree Add')
    plt.plot(xlabels, values_binarytree_min, color='g', linestyle='--', label='binarytree Get Min')
    plt.plot(xlabels, values_binarytree_max, color='g', linestyle='-.', label='binarytree Get Max')
    plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Heap Add')

    plt.plot(xlabels, values_quicksort_add, color='r', linestyle='-', label='quicksort Add')
    plt.plot(xlabels, values_quicksort_min, color='r', linestyle='--', label='quicksort Get Min')
    plt.plot(xlabels, values_quicksort_max, color='r', linestyle='-.', label='quicksort Get Max')
    plt.plot(xlabels, values_bubble_min, color='y', linestyle='--', label='Heap Get Min')

    plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
    plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min')
    plt.plot(xlabels, values_heap_max, color='b', linestyle='-.', label='Heap Get Max')
    plt.plot(xlabels, values_bubble_max, color='y', linestyle='-.', label='Heap Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of binarytree, quicksort, Heap solutions")
    plt.show()