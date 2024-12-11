def count_xmas(grid, word="XMAS"):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),   # Horizontal (right)
        (1, 0),   # Vertical (down)
        (1, 1),   # Diagonal (down-right)
        (1, -1),  # Diagonal (down-left)
        (0, -1),  # Horizontal (left)
        (-1, 0),  # Vertical (up)
        (-1, -1), # Diagonal (up-left)
        (-1, 1)   # Diagonal (up-right)
    ]

    def is_valid(x, y):
        """Check if (x, y) is within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def count_in_direction(x, y, dx, dy):
        """Count occurrences of the word starting from (x, y) in direction (dx, dy)."""
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return 0
        return 1

    total_count = 0

    # Loop through each cell in the grid
    for x in range(rows):
        for y in range(cols):
            # Check all directions from the current position
            for dx, dy in directions:
                total_count += count_in_direction(x, y, dx, dy)

    return total_count

if __name__ == "__main__":
# Example input grid
    with open ('raw_data4.txt', 'r') as file:
        grid = file.readlines()

    # Count occurrences of "XMAS"
    result = count_xmas(grid)
    print(f"The word 'XMAS' occurs {result} times in the grid.")
