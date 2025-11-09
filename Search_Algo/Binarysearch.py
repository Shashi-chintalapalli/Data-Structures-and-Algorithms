class BinarySearch:
    
    def __init__(self,num,find):
        self.num=num
        self.find=find
        
    def Binary_search(self):
        left=0
        right=len(self.num)-1
        while left<=right:
            mid=(left+right)//2
            if self.num[mid]==self.find:
                return mid
            elif self.find<self.num[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1

search=BinarySearch([1,2,3,4,6,8,11],8)
print(search.Binary_search())
            
                
    