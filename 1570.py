# Dot Product of Two Sparse Vectors

class SparseVector:
    def __init__(self, nums: List[int]):
        #self.vector = nums

        self.pairs = {}
        
        for i,j in enumerate(nums):
            if j!=0:
                self.pairs[i] = j    
        
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int: 
    
        #return sum([i*j for i,j in zip(self.vector, vec.vector)])
        ans = 0
    
        for i,j in self.pairs.items():
            if i in vec.pairs:
                ans += j*vec.pairs[i]
                
        return ans


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
