# Reduce Array Size to The Half

from collections import Counter
import math

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # new_arr = arr
        # counter = 0
        # while(len(new_arr)>(len(arr)/2)):
        #     counts = Counter(new_arr)
        #     max_count_num = max(counts, key= lambda x: counts[x])
        #     counter += 1
        #     new_arr = [i for i in new_arr if i != max_count_num]
        # return counter

        # arr = sorted(arr, key = arr.count, reverse = True)
        # return len(set(arr[:(int(math.ceil(len(arr)/2)))]))

        counts = list(Counter(arr).values())
        counts.sort(reverse=True)
        half = len(arr)/2
        c = 0
        for i in counts:
            half -= i
            c += 1

            if(half <= 0):
                return c
