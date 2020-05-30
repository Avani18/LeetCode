# Flood Fill
# https://leetcode.com/problems/flood-fill
'''An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.'''


def floodFill(image, sr, sc, newColor):
        if newColor == image[sr][sc]:
            return image
        
        parent = image[sr][sc]
        
        def flood(sr, sc):
            if parent != image[sr][sc]:
                return            

            image[sr][sc] = newColor
            if sr+1 <= len(image)-1:
                flood(sr+1, sc)
            if sr-1 >= 0:    
                flood(sr-1, sc)            
            if sc+1 <= len(image[sr])-1:
                flood(sr, sc+1)
            if sc-1 >= 0:    
                flood(sr, sc-1)
        
        flood(sr,sc )
        return image
        
print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
