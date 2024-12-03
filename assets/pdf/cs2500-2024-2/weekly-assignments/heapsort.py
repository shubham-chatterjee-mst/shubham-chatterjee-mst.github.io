def max_heapify(arr, n, i):
    # Step 1: Define left and right children of node at index i
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    # TODO: Check if left child exists and is greater than root
   
    # TODO: Check if right child exists and is greater than current largest
    
    # TODO: Swap and continue heapifying if root is not largest
   
def build_max_heap(arr):
    n = len(arr)
    # TODO: Build the max heap by calling max_heapify on each non-leaf node
    
def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max heap from the input array
    build_max_heap(arr)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # TODO: Move current root to the end
       
        # TODO: Call max_heapify on the reduced heap
       
# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)
