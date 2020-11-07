# Build an Array With Stack Operations


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        ops = []
        for i in range(1,n+1):
            if i in target:
                ops.append("Push")
                ans.append(i)
            else:
                ops.append("Push")
                ops.append("Pop")
            if ans == target:
                break
        return ops
