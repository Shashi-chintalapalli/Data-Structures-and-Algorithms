class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def merge_sort(self, arr=None):
        if arr is None:
            arr = self.arr

        # Base case
        if len(arr) <= 1:
            return arr

        # Divide step
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive sort
        sorted_left = self.merge_sort(left_half)
        sorted_right = self.merge_sort(right_half)

        # Merge step
        return self.merge(sorted_left, sorted_right)

    def merge(self, left, right):
        result = []
        i = j = 0

        # Compare and merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result


# Example usage
val = MergeSort([2, 3, 2, 11, 23, 12, 4])
print(val.merge_sort())


# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr
#     mid=len(arr)//2
#     left=arr[:mid]
#     right=arr[mid:]
#     sorted_left=merge_sort(left)
#     sorted_right=merge_sort(right)
#     return merge(sorted_left,sorted_right)
# def merge(left,right):
#     result=[]
#     i=j=0
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# print(merge_sort([2, 3, 2, 11, 23, 12, 4]))