"""
Experiment 9: Dynamic Array Simulation
Demonstrates resizing with amortized O(1) append
"""

class DynamicArray:
    def __init__(self, initial_capacity=2):
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity
        self.resize_count = 0
    
    def append(self, value):
        """Append with doubling resize strategy"""
        if self.size == self.capacity:
            # Resize: double the capacity
            self.resize_count += 1
            old_capacity = self.capacity
            self.capacity *= 2
            new_array = [None] * self.capacity
            
            # Copy elements
            for i in range(self.size):
                new_array[i] = self.array[i]
            
            self.array = new_array
            print(f"  → Resize triggered! {old_capacity} → {self.capacity}")
        
        self.array[self.size] = value
        self.size += 1
        print(f"  Append {value}: size={self.size}, capacity={self.capacity}")
    
    def pop(self):
        """Pop from end (no shrink for simplicity)"""
        if self.size == 0:
            raise IndexError("Pop from empty array")
        
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        print(f"  Pop: {value}, size={self.size}, capacity={self.capacity}")
        return value
    
    def get(self, index):
        """Access element by index - O(1)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]
    
    def display(self):
        elements = [self.array[i] for i in range(self.size)]
        print(f"DynamicArray: {elements}, size={self.size}, capacity={self.capacity}")
        return elements
    
    def amortized_analysis(self, n):
        """Demonstrate amortized O(1) by appending n elements"""
        print(f"\n--- Amortized Analysis: Appending {n} elements ---")
        print(f"Initial capacity: {self.capacity}")
        
        import time
        start_time = time.time()
        
        for i in range(n):
            self.append(i)
        
        elapsed = time.time() - start_time
        print(f"\nResult: {self.size} elements, capacity={self.capacity}")
        print(f"Resize events: {self.resize_count}")
        print(f"Total time: {elapsed:.6f} seconds")
        print(f"Amortized cost per append: O(1)")
        
        # Theoretical explanation
        print("\n--- Amortized Complexity Explanation ---")
        print("For n appends with doubling strategy:")
        print("  - Resizes occur at sizes: 2, 4, 8, 16, ..., up to n")
        print("  - Cost of each resize: O(current size)")
        print("  - Total resize cost: 2 + 4 + 8 + ... + n = O(n)")
        print("  - Total cost: n appends + O(n) resizes = O(n)")
        print("  - Average cost per append: O(1)")

# Test Experiment 9
print("="*50)
print("Experiment 9: Dynamic Array Simulation")
print("="*50)

# Test 1: Basic operations
print("\n--- Test 1: Basic Operations ---")
da = DynamicArray(2)
da.append(10)
da.append(20)
da.append(30)
da.append(40)
da.append(50)
da.display()
da.pop()
da.pop()
da.display()

# Test 2: Amortized analysis
print("\n--- Test 2: Amortized Analysis ---")
da2 = DynamicArray(2)
da2.amortized_analysis(10)

# Test 3: Access O(1) demonstration
print("\n--- Test 3: O(1) Index Access ---")
da3 = DynamicArray(4)
for i in range(10):
    da3.append(i)

print(f"Element at index 0: {da3.get(0)}")
print(f"Element at index 5: {da3.get(5)}")
print(f"Element at index 9: {da3.get(9)}")
print("All accesses completed in O(1) time regardless of array size")