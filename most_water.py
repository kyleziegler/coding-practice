# Kyle Ziegler 5/2021


# Description
# Given n non-negative integers a1, a2, ..., an , where each 
# represents a point at coordinate (i, ai). n vertical lines 
# are drawn such that the two endpoints of the line i is at (i, ai) 
# and (i, 0). Find two lines, which, together with the x-axis forms
#  a container, such that the container contains the most water.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Max height
        m = 0
        # Init pointers
        p1 = 0
        p2 = len(height)-1
        
        # keep the pointer that is at the greater height
        # in place, and move the lesser pointer
        
        while(p1 != p2):            
            # print("pointers", p1,p2)
            # print(height[p1],height[p2])
            
            # Sanity check to ensure we're not out of bounds on our 
            # pointers
            if(p1 > len(height)-1 or p2 < 1):
                return m
            
            c = min(height[p1],height[p2]) * (p2-p1)
            m = max(c, m)

            if (height[p1] > height[p2]):
                # decrement p2
                p2 -= 1
                continue
            elif (height[p1] < height[p2]):
                # increment p1
                p1 += 1
            elif(len(height) == 2):
                return m
            else:
                p1 += 1
                p2 -= 1
        return m