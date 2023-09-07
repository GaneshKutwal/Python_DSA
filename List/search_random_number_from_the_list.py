def kth_smallest(arr, k):
    if k <= 0 or k > len(arr):
        return None  # Invalid input, k out of range

    arr.sort()  # Sort the list in O(n log n) time

    return arr[k - 1]  # kth smallest element is at index k-1

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 4
kth_smallest_element = kth_smallest(arr, k)
print(f"The {k}th smallest element is {kth_smallest_element}")
