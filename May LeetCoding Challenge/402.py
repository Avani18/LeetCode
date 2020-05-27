# Remove K Digits
# https://leetcode.com/problems/remove-k-digits/
''' Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.'''

def removeKdigits(num, k):
        
        st, required = [], k
        for x in num:
            while required and st and st[-1] > x:
                st.pop()
                required = required-1
            st.append(x)
        result = "".join(st[0:len(num)-k]).lstrip("0")
        return result if len(result) else "0"
        
print (removeKdigits("1432219", 3))
