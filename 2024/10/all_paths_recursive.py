def find_all_incremental_paths(matrix, row, col, current_value=0, current_path=None):
    """
    Find all possible paths of incrementing values (0->1->2...) in a matrix.
    Returns a list of all valid paths.
    """
    if current_path is None:
        current_path = []
    
    # Boundary checks
    if (row < 0 or row >= len(matrix) or 
        col < 0 or col >= len(matrix[0]) or 
        matrix[row][col] != current_value):
        return []
    
    # Add current position to path
    current_path = current_path + [(row, col)]
    
    # If we've reached 9, we've found a complete path
    if current_value == 9:
        return [current_path]
    
    # Find all possible continuations
    all_paths = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        paths = find_all_incremental_paths(matrix, new_row, new_col, 
                                         current_value + 1, current_path)
        all_paths.extend(paths)
    
    return all_paths

# Example usage with a matrix that has multiple possible paths
matrix = [
    [0, 1, 2, 3],
    [1, 6, 5, 4],
    [2, 7, 6, 5],
    [9, 8, 9, 9]
]
import sys
matrix = []
with open(sys.argv[1]) as f:
    for line in f.readlines():
        matrix.append([int(x) for x in line.strip()])

#print(matrix)

# Find all paths starting from 0
all_paths = []
path_map = {}
distinct_path = {}
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            paths = find_all_incremental_paths(matrix, i, j)
            all_paths.extend(paths)
            #breakpoint()
            path_map[(i,j)] = len(set([x[-1] for x in paths]))
            distinct_path[(i,j)] = len(paths)

# Print all found paths
#for i, path in enumerate(all_paths, 1):
#    print(f"Path {i}:", path)

# Visualize one of the paths in the matrix
def visualize_path(matrix, path):
    """Helper function to visualize a path in the matrix"""
    rows, cols = len(matrix), len(matrix[0])
    result = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    # Fill in the path with arrow symbols
    for idx, (row, col) in enumerate(path):
        result[row][col] = str(matrix[row][col])
        
    return '\n'.join([''.join(f'{cell:>2}' for cell in row) for row in result])

if all_paths:
    print("\nVisualization of first path:")
    #for x in all_paths:
    #print(visualize_path(matrix, all_paths[0]))
    #print(visualize_path(matrix, all_paths[1]))
    #print(visualize_path(matrix, all_paths[2]))
    #print(visualize_path(matrix, all_paths[3]))
    #print(visualize_path(matrix, all_paths[4]))
        #print(visualize_path(matrix, x))
    #print(visualize_path(matrix, all_paths[5]))
    #print(visualize_path(matrix, all_paths[6]))
        #print("**************")

print(f"Path map: {path_map}")
# NEed to get the unique set of final spots
print(f"Sum: {sum(path_map.values())}")
print(f"Distinct paths: {sum(distinct_path.values())}")
