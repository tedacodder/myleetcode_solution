class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
         # Sort children's greed and cookie sizes
        g.sort()
        s.sort()
        
        # i = index for children (greed)
        # j = index for cookies (sizes)
        i = 0
        j = 0
        count = 0
        
        # Greedy: satisfy the least greedy child with the smallest cookie possible
        while i < len(g) and j < len(s):
            
            # If the current cookie can satisfy the child
            if s[j] >= g[i]:
                count += 1      # child is satisfied
                i += 1          # move to next child
                j += 1          # move to next cookie
            
            else:
                # Cookie too small → try next larger cookie
                j += 1

        return count