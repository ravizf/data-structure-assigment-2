"""
Experiment 7: Arrays 1D Operations with Shifting Cost Analysis
Demonstrates cost of insert/delete operations in static arrays
"""

class Array1D:
    def __init__(self, size=10):
        self.array = [None] * size
        self.size = 0
        self.capacity = size
    
    def insert_at_start(self, value):
        """Insert at beginning - shifts all elements right"""
        if self.size == self.capacity:
            print("Array full! Cannot insert.")
            return
        
        shift_count = self.size
        for i in range(self.size, 0, -1):
            self.array[i] = self.array[i-1]
        
        self.array[0] = value
        self.size += 1
        print(f"Insert {value} at start: {shift_count} shifts")
        return shift_count
    
    def insert_at_middle(self, value, pos):
        """Insert at given position - shifts elements after pos"""
        if self.size == self.capacity:
            print("Array full! Cannot insert.")
            return
        
        if pos < 0 or pos > self.size:
            print("Invalid position")
            return
        
        shift_count = self.size - pos
        for i in range(self.size, pos, -1):
            self.array[i] = self.array[i-1]
        
        self.array[pos] = value
        self.size += 1
        print(f"Insert {value} at position {pos}: {shift_count} shifts")
        return shift_count
    
    def insert_at_end(self, value):
        """Insert at end - no shifts needed"""
        if self.size == self.capacity:
            print("Array full! Cannot insert.")
            return
        
        self.array[self.size] = value
        self.size += 1
        print(f"Insert {value} at end: 0 shifts")
        return 0
    
    def delete_at_start(self):
        """Delete from beginning - shifts all elements left"""
        if self.size == 0:
            print("Array empty!")
            return
        
        value = self.array[0]
        shift_count = self.size - 1
        
        for i in range(1, self.size):
            self.array[i-1] = self.array[i]
        
        self.array[self.size-1] = None
        self.size -= 1
        print(f"Delete {value} from start: {shift_count} shifts")
        return value, shift_count
    
    def delete_at_middle(self, pos):
        """Delete from given position - shifts elements after pos"""
        if self.size == 0:
            print("Array empty!")
            return
        
        if pos < 0 or pos >= self.size:
            print("Invalid position")
            return
        
        value = self.array[pos]
        shift_count = self.size - pos - 1
        
        for i in range(pos, self.size-1):
            self.array[i] = self.array[i+1]
        
        self.array[self.size-1] = None
        self.size -= 1
        print(f"Delete {value} from position {pos}: {shift_count} shifts")
        return value, shift_count
    
    def delete_at_end(self):
        """Delete from end - no shifts needed"""
        if self.size == 0:
            print("Array empty!")
            return
        
        value = self.array[self.size-1]
        self.array[self.size-1] = None
        self.size -= 1
        print(f"Delete {value} from end: 0 shifts")
        return value, 0
    
    def display(self):
        print(f"Array: {[self.array[i] for i in range(self.size)]}")
        print(f"Size: {self.size}, Capacity: {self.capacity}")
        print()


# Test Experiment 7
print("="*50)
print("Experiment 7: Arrays 1D Operations")
print("="*50)

arr = Array1D(8)

# Test inserts
print("\n--- Insert Operations ---")
arr.insert_at_end(10)      # End insert: 0 shifts
arr.insert_at_end(20)      # End insert: 0 shifts
arr.insert_at_end(30)      # End insert: 0 shifts
arr.insert_at_start(5)     # Start insert: 3 shifts
arr.insert_at_middle(15, 2) # Middle insert at index 2: shifts elements after
arr.display()

# Test deletes
print("\n--- Delete Operations ---")
arr.delete_at_end()        # End delete: 0 shifts
arr.delete_at_start()      # Start delete: shifts all left
arr.delete_at_middle(1)    # Delete at position 1: shifts after
arr.display()

print("\n--- Complexity Summary ---")
print("| Operation | Time Complexity | Shifts Required |")
print("|-----------|-----------------|-----------------|")
print("| Insert at start | O(n) | n |")
print("| Insert at middle | O(n) | n - pos |")
print("| Insert at end | O(1) | 0 |")
print("| Delete at start | O(n) | n-1 |")
print("| Delete at middle | O(n) | n-pos-1 |")
print("| Delete at end | O(1) | 0 |")
print("| Access by index | O(1) | 0 |")