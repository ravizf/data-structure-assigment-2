"""
Experiment 8: Arrays 2D Matrix Operations
Demonstrates row/column traversal, search, and transpose
"""

class Matrix2D:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0
    
    def row_sum(self, row_idx):
        """Calculate sum of a specific row"""
        if row_idx >= self.rows:
            return None
        return sum(self.matrix[row_idx])
    
    def all_row_sums(self):
        """Calculate sum of all rows"""
        return [sum(row) for row in self.matrix]
    
    def col_sum(self, col_idx):
        """Calculate sum of a specific column"""
        if col_idx >= self.cols:
            return None
        return sum(self.matrix[row][col_idx] for row in range(self.rows))
    
    def all_col_sums(self):
        """Calculate sum of all columns"""
        return [sum(self.matrix[row][col] for row in range(self.rows)) 
                for col in range(self.cols)]
    
    def search(self, value):
        """Search for a value in the matrix"""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == value:
                    return (i, j)
        return None
    
    def transpose(self):
        """Return transpose of matrix"""
        transposed = [[self.matrix[i][j] for i in range(self.rows)] 
                      for j in range(self.cols)]
        return transposed
    
    def display(self):
        """Display matrix with formatting"""
        print("Matrix:")
        for row in self.matrix:
            print("  ", row)
        print()


# Test Experiment 8
print("="*50)
print("Experiment 8: Arrays 2D Matrix Operations")
print("="*50)

# Create a 3x4 matrix
matrix_data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

mat = Matrix2D(matrix_data)
mat.display()

print("--- Row Operations ---")
print(f"Row 0 sum: {mat.row_sum(0)}")
print(f"Row 1 sum: {mat.row_sum(1)}")
print(f"Row 2 sum: {mat.row_sum(2)}")
print(f"All row sums: {mat.all_row_sums()}")

print("\n--- Column Operations ---")
print(f"Column 0 sum: {mat.col_sum(0)}")
print(f"Column 1 sum: {mat.col_sum(1)}")
print(f"Column 2 sum: {mat.col_sum(2)}")
print(f"Column 3 sum: {mat.col_sum(3)}")
print(f"All column sums: {mat.all_col_sums()}")

print("\n--- Search Operations ---")
print(f"Search 7: Found at {mat.search(7)}")
print(f"Search 20: {mat.search(20)}")

print("\n--- Transpose ---")
transposed = mat.transpose()
print("Original matrix: 3x4")
print("Transposed matrix: 4x3")
for row in transposed:
    print("  ", row)

print("\n--- Complexity Analysis ---")
print("| Operation | Time Complexity | Space Complexity |")
print("|-----------|-----------------|------------------|")
print("| Row sum | O(cols) | O(1) |")
print("| All row sums | O(rows * cols) | O(rows) |")
print("| Column sum | O(rows) | O(1) |")
print("| All column sums | O(rows * cols) | O(cols) |")
print("| Search | O(rows * cols) | O(1) |")
print("| Transpose | O(rows * cols) | O(rows * cols) |")