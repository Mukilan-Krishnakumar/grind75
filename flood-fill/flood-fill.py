from typing import List
class Solution:        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        start_color = image[sr][sc]

        def flood_fill(x,y):
            if x < 0 or x >= len(image) or y < 0 or y>= len(image[0]):
                return
            if image[x][y] == color:
                return 
            if image[x][y] != start_color:
                return
            # Change the value only if the current value equals the start color
            image[x][y] = color
            # Top    
            flood_fill(x-1,y)
            # Left
            flood_fill(x,y-1)
            # Bottom
            flood_fill(x+1,y)
            # Right
            flood_fill(x,y+1)

        flood_fill(sr, sc)
        return image

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
