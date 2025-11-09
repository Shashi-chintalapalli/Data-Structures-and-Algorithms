class TwoSum:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    def two_sum(self):
        seen={}
        for i,num in enumerate(self.arr):
            complement=self.target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i
        return [-1,-1]
val = TwoSum([2, 7, 11, 15,23], 22)
print(val.two_sum())
        