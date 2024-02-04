# An ant is on a boundary. It sometimes goes left and sometimes right.

# You are given an array of non-zero integers nums. The ant starts reading nums from the first element of it to its end. At each step, it moves according to the value of the current element:

# If nums[i] < 0, it moves left by -nums[i] units.
# If nums[i] > 0, it moves right by nums[i] units.
# Return the number of times the ant returns to the boundary.

# Notes:

# There is an infinite space on both sides of the boundary.
# We check whether the ant is on the boundary only after it has moved |nums[i]| units. In other words, if the ant crosses the boundary during its movement, it does not count.

# Input: nums = [2,3,-5]
# Output: 1
# Explanation: After the first step, the ant is 2 steps to the right of the boundary.
# After the second step, the ant is 5 steps to the right of the boundary.
# After the third step, the ant is on the boundary.
# So the answer is 1.

# Input: nums = [3,2,-3,-4]
# Output: 0
# Explanation: After the first step, the ant is 3 steps to the right of the boundary.
# After the second step, the ant is 5 steps to the right of the boundary.
# After the third step, the ant is 2 steps to the right of the boundary.
# After the fourth step, the ant is 2 steps to the left of the boundary.
# The ant never returned to the boundary, so the answer is 0.

import math
def minimumTimeToInitialState(self, word: str, k: int) -> int:
    i = k
    ans = 1
    maxTime = ceil(len(word)/k)    

    while ans<maxTime:
        if word[:len(word)-i]==word[i:len(word)]:
            return 0
        ans+=1
        i+=k
        
    return ans

    n=len(word)
    for i in range(k,n+1,k):
        if word[i:]==word[:-i]:
            return i//k
    return (n+k-1)//k

# word[:len(word)-i]==word[i:len(word)]:
# This line checks if the first half of the string is equal to the second half of the string


# for input abacaba and k = 3

# i = 3
# ans = 1
# maxTime = 7/3 = 3

# word[:len(word)-i] = word[:7-3] = word[:4] = abac
# word[i:len(word)] = word[3:7] = word[3:] = caba

# ans = 2
# i = 6
# word[:len(word)-i] = word[:7-6] = word[:1] = a
# word[i:len(word)] = word[6:7] = word[6:] = a

# break

# ans = 2
# return 2


# for input abacaba and k = 4

# i = 4
# ans = 1
# maxTime = 7/4 = 2

# word[:len(word)-i] = word[:7-4] = word[:3] = aba
# word[i:len(word)] = word[4:7] = word[4:] = aba
# shouldn't it break here? //yes, it should have broken here but it didn't 


# ans = 2
# i = 8
# word[:len(word)-i] = word[:7-8] = word[:0] = 
# word[i:len(word)] = word[8:7] = word[8:] = 

# break //why didn't it break at the first iteration? 

# ans = 2
# return 2



