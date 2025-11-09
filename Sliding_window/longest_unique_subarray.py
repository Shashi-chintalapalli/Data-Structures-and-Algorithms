def longest_unique_subarray(arr):
    start=0
    dist_element=set()
    max_len=0
    for end in range(0,len(arr)):
        while arr[end] in dist_element:
            dist_element.remove(arr[start])
            start+=1
        dist_element.add(arr[end])
        max_len=max(max_len,end-start+1)
    return max_len
print(longest_unique_subarray([1,2,3,1,2,3,2,2]))