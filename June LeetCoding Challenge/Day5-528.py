# Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/
'''Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.'''

def __init__(self, w: List[int]):
        length = len(w)
        self.probabilities = [0] * length
        
        total_weight = sum(w)
        running_probability = 0.0
        
        for i, weight in enumerate(w):
            probability = weight / total_weight
            running_probability += probability
            self.probabilities[i] = running_probability
        
        # print(self.probabilities)
        
        

def pickIndex(self) -> int:
        rand_number_between_0_and_1 = random.random()
        binary_search_result = bisect_left(self.probabilities, rand_number_between_0_and_1)
        # print(rand_number_between_0_and_1, " --> ",  binary_search_result)
        return binary_search_result
