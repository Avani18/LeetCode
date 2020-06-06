# Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/
'''Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.'''

def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        stack = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
        res = [None for _ in people]
        while stack:
            h, k = stack.pop()
            target, idx = k + 1, 0
            while target:
                if res[idx] is None:
                    target -= 1
                idx += 1
            res[idx-1] = (h, k)
        return res
