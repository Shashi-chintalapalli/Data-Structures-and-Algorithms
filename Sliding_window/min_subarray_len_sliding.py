def min_subarray_len(arr,target):
    n=len(arr)
    start=0
    window_sum=0
    min_len=float('inf')
    for end in range(0,n):
        window_sum+=arr[end]
        while window_sum>=target:
            window_len=end-start+1
            min_len=min(window_len,min_len)
            window_sum-=arr[start]
            start+=1
    return min_len

print(min_subarray_len([2,3,1,2,4,3],7))
