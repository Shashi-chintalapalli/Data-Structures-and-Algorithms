# # Creating lists
# arr = [10, 20, 30, 40, 50]

# # Access elements
# print(arr[0])   # 10
# print(arr[-1])  # 50 (last element)

# # Add elements
# arr.append(60)        # Add at end
# arr.insert(2, 25)     # Insert at index 2

# # Remove elements
# arr.pop()             # Removes last element (60)
# arr.remove(25)        # Removes first occurrence of 25

# # Update element
# arr[1] = 99

# print(arr)  # [10, 99, 30, 40, 50]


def maximun(num):
    max=num[0]
    for i in num:
        if i > max:
            max=i
    return max 
arr = [5, 3, 9, 1, 7]
val = maximun(arr)
print(val)
