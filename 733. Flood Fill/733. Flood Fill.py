class Solution:
    def floodFill(self, image, sr, sc, color):
        start_color = image[sr][sc]
        if start_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            image[r][c] = color
            
            for i in range(rows):
                for j in range(cols):
                    is_adjacent = abs(i - r) + abs(j - c) == 1
                    if is_adjacent and image[i][j] == start_color:
                        dfs(i, j)

        dfs(sr, sc)
        return image
