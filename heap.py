class HeapBase(object):

    def __init__(self, l=None):
        self.heap = l if l else []
        self.heap_size = len(l) if l else 0

    def __str__(self):
        return "{}".format(self.heap)

    def parent_i(self, i):
        return i//2 if i%2 else i//2-1

    def left_i(self, i):
        return i*2+1

    def right_i(self, i):
        return i*2+2


class MaxHeapMixin(object):
    def max_heapify_down(self, i):
        """Swap a key with its child if its child's key's larger,
        and keep doing it down the tree recursively until reaching a
        leaf or until the parent's key is larger than its children's"""
        left_i, right_i = self.left_i(i), self.right_i(i)
        largest_i = i
        if left_i < self.heap_size and self.heap[left_i] > self.heap[i]:
            largest_i = left_i
        if right_i < self.heap_size and self.heap[right_i] > self.heap[largest_i]:
            largest_i = right_i
        if largest_i != i:
            self.heap[i], self.heap[largest_i] =self.heap[largest_i], self.heap[i]
            self.max_heapify_down(largest_i)

    def build_max_heap(self):
        for i in range(len(self.heap)//2-1, -1, -1):
            self.max_heapify_down(i)


class MinHeapMixin(object):
    def min_heapify_down(self, i):
        """Swap a key with its child if its child's key's smaller,
        and keep doing it down the tree recursively until reaching a
        leaf or until the parent's key is smaller than its children's"""
        left_i, right_i = self.left_i(i), self.right_i(i)
        smallest_i = i
        if left_i < self.heap_size and self.heap[left_i] < self.heap[i]:
            smallest_i = left_i
        if right_i < self.heap_size and self.heap[right_i] < self.heap[smallest_i]:
            smallest_i = right_i
        if smallest_i != i:
            self.heap[i], self.heap[smallest_i] =self.heap[smallest_i], self.heap[i]
            self.min_heapify_down(smallest_i)

    def build_min_heap(self):
        for i in range(len(self.heap)//2-1, -1, -1):
            self.min_heapify_down(i)


class MaxHeapSort(MaxHeapMixin, HeapBase):
    "Sorts an array in the increasing order in place."
    def __init__(self, l=None):
        super().__init__(l=l)
        self.sort_maxheap()

    def sort_maxheap(self):
        self.build_max_heap()
        for i in range(len(self.heap)-1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heap_size -= 1
            self.max_heapify_down(0)


class MinHeapSort(MinHeapMixin, HeapBase):
    "Sorts an array in the decreasing order in place."
    def __init__(self, l=None):
        super().__init__(l=l)
        self.sort_minheap()

    def sort_minheap(self):
        self.build_min_heap()
        for i in range(len(self.heap)-1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heap_size -= 1
            self.min_heapify_down(0)


class MaxHeap(MaxHeapMixin, HeapBase):
    def __init__(self, l=None):
        super().__init__(l=l)
        self.build_max_heap()

    def heap_maximum(self):
        return self.heap[0]

    def extract_heap_maximum(self):
        if len(self.heap) > 0:
            m = self.heap[0]
        else:
            raise IndexError
        last_in_heap = self.heap[self.heap_size-1]
        self.heap[0] = last_in_heap
        self.heap_size -= 1
        self.max_heapify_down(0)
        return m

    def max_heapify_up(self, i):
        parent_i = self.parent_i(i)
        if parent_i < 0: return
        if self.heap[parent_i] < self.heap[i]:
            self.heap[parent_i], self.heap[i] = self.heap[i], self.heap[parent_i]
            self.max_heapify_up(parent_i)

    def increase_key(self, i, key):
        if not i in range(len(self.heap)):
            raise IndexError("\nThe index is out of range\n")
        if self.heap[i] >= key:
            raise ValueError("\nThe new key isn't greater than the current one\n")
        self.heap[i] = key
        self.max_heapify_up(i)

    def insert_key(self, key):
        "Insert a key and enforce the max heap property"
        try:
            self.heap[self.heap_size] = key
        except IndexError:
            self.heap.append(key)
        self.heap_size += 1
        self.max_heapify_up(self.heap_size-1)


class MinHeap(MinHeapMixin, HeapBase):
    def __init__(self, l=None):
        super().__init__(l=l)
        self.build_min_heap()

    def heap_minimum(self):
        return self.heap[0]

    def extract_heap_minimum(self):
        if len(self.heap) > 0:
            m = self.heap[0]
        else:
            raise IndexError
        last_in_heap = self.heap[self.heap_size-1]
        self.heap[0] = last_in_heap
        self.heap_size -= 1
        self.min_heapify_down(0)
        return m

    def min_heapify_up(self, i):
        parent_i = self.parent_i(i)
        if parent_i < 0: return
        if self.heap[parent_i] > self.heap[i]:
            self.heap[parent_i], self.heap[i] = self.heap[i], self.heap[parent_i]
            self.min_heapify_up(parent_i)

    def decrease_key(self, i, key):
        if not i in range(len(self.heap)):
            raise IndexError("\nThe index is out of range\n")
        if self.heap[i] <= key:
            print("self.heap[i]:", self.heap[i], "- i:", i)
            raise ValueError("\nThe new key isn't lesser than the current one\n")
        self.heap[i] = key
        self.min_heapify_up(i)

    def insert_key(self, key):
        "Insert a key and enforce the min heap property"
        try:
            self.heap[self.heap_size] = key
        except IndexError:
            self.heap.append(key)
        self.heap_size += 1
        self.min_heapify_up(self.heap_size-1)

