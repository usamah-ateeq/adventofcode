with open('4.txt','r') as ff:
    input_file = ff.read()

grid = input_file.splitlines()


def find_xmas(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1), # Left
        (-1, 0), # Up
        (1, 1),  # Down-right (Diagonal)
        (-1, -1),# Up-left (Diagonal)
        (1, -1), # Down-left (Diagonal)
        (-1, 1)  # Up-right (Diagonal)
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, direction):
        dx, dy = direction
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    found_positions = []

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == word[0]:  # Match first letter
                for direction in directions:
                    if search_from(x, y, direction):
                        found_positions.append((x, y))

    return found_positions

# Search for "XMAS"
word = "XMAS"
results = find_xmas(grid, word)

# Print the results
print("Found XMAS at positions:", len(results))
