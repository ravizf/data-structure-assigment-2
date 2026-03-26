# data-structure-assigment-2 <br>
Name: Ravi <br>
Roll no : 2501010129 <br>
Course Code: ETCCDS202 <br>
Program: B.Tech (CSE ) section A <br>
School: School of Engineering & Technology <br>
Course: Data Structures <br>
Semester: B.Tech <br>
Year: 2026 <br>
Data Structures Lab Manual - Unit 2: Linear Data Structures

📚 Overview

This repository contains complete implementations of all Unit 2 experiments from the Data Structures Lab Manual (2026). Each experiment demonstrates fundamental linear data structures with comprehensive code, complexity analysis, and practical applications.

📁 Repository Structure

```
unit-2-linear-data-structures/
│
├── experiment_07_arrays_1d.py          # Array operations with shifting cost analysis
├── experiment_08_arrays_2d.py          # Matrix operations (row/col sums, transpose)
├── experiment_09_dynamic_array.py      # Dynamic array with amortized analysis
├── experiment_10_singly_linked_list.py # SLL with head/tail management
├── experiment_11_doubly_linked_list.py # DLL with bidirectional traversal
├── experiment_12_stack_parentheses.py  # Stack implementation + parentheses checker
├── experiment_13_queue_bfs.py          # Queue implementation + BFS simulation
│
├── README.md                           # This file
└── COMPLEXITY_SUMMARY.md               # Detailed complexity analysis
```

🎯 Experiments Covered

# Experiment Key Concepts Time Complexity
7 Arrays 1D Insert/delete operations, shifting cost O(1) access, O(n) shift
8 Arrays 2D Matrix traversal, row/col sums, transpose O(rows × cols)
9 Dynamic Array Doubling resize, amortized analysis O(1) amortized append
10 Singly Linked List Insert at head/tail, delete by value O(1) insert at ends
11 Doubly Linked List Insert after node, delete at position O(1) pointer updates
12 Stack (SLL) Push/pop/peek, parentheses checker O(1) all operations
13 Queue (SLL) Enqueue/dequeue, BFS simulation O(1) all operations

🚀 Getting Started

Prerequisites

· Python 3.7 or higher
· No external libraries required

Running the Experiments

```bash
# Clone the repository
git clone https://github.com/yourusername/unit-2-linear-data-structures.git
cd unit-2-linear-data-structures

# Run any experiment
python experiment_07_arrays_1d.py
python experiment_08_arrays_2d.py
# ... and so on
```

Running All Tests

```bash
# Run all experiments sequentially
for file in experiment_*.py; do
    echo "Running $file..."
    python "$file"
    echo "------------------------"
done
```

📊 Key Implementations

1. Dynamic Array with Amortized Analysis

```python
class DynamicArray:
    def append(self, value):
        if self.size == self.capacity:
            self.capacity *= 2  # Doubling strategy
            # Resize and copy
        # O(1) amortized
```

2. Singly Linked List with Tail Pointer

```python
class SinglyLinkedList:
    def insert_at_end(self, data):
        # O(1) with tail pointer
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
```

3. Stack for Parentheses Checking

```python
def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.pop() != matching(char):
                return False
    return stack.is_empty()
```

4. Queue for BFS Traversal

```python
def bfs(graph, start):
    queue = Queue()
    queue.enqueue(start)
    visited = {start}
    while not queue.is_empty():
        vertex = queue.dequeue()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
```

📈 Complexity Summary

Data Structure Operation Best Case Average Case Worst Case
Static Array Access O(1) O(1) O(1)
 Insert at start O(n) O(n) O(n)
 Insert at end O(1) O(1) O(1)
Dynamic Array Append O(1) O(1) amortized O(n) resize
 Pop O(1) O(1) O(1)
SLL Insert head O(1) O(1) O(1)
 Insert tail O(1) with tail O(1) O(1)
 Delete by value O(1) O(n) O(n)
DLL Insert after node O(n) to find O(n) O(n)
 Delete at position O(n) to reach O(n) O(n)
Stack Push/Pop/Peek O(1) O(1) O(1)
Queue Enqueue/Dequeue O(1) O(1) O(1)

💡 Real-World Applications

· Stack: Function call management, undo/redo, expression evaluation, browser back button
· Queue: Print spoolers, task scheduling, BFS in social networks, request processing
· Linked Lists: Music playlists, image viewers, browser history
· Dynamic Arrays: Python lists, ArrayList in Java, vector in C++
· 2D Arrays: Image processing, spreadsheet data, game boards

🧪 Sample Output

```
==================================================
Experiment 7: Arrays 1D Operations
==================================================

--- Insert Operations ---
Insert 10 at end: 0 shifts
Insert 20 at end: 0 shifts
Insert 30 at end: 0 shifts
Insert 5 at start: 3 shifts
Array: [5, 10, 20, 30], Size: 4

--- Parentheses Checker ---
Checking: '{[()]}'
  Push: {
  Push: [
  Push: (
  Pop: ( matches )
  Pop: [ matches ]
  Pop: { matches }
✓ BALANCED
```

📝 Viva Questions Covered

Each experiment includes answers to common viva questions:

1. Arrays: Why is index access O(1)? Why insertion at start is O(n)?
2. Linked Lists: Why search is O(n)? DLL vs SLL advantages?
3. Stack: Why stack for parentheses? Real-world uses?
4. Queue: Why BFS uses queue? FIFO meaning?
5. Amortized Analysis: Why doubling helps? Amortized vs average?

🔍 Testing

Each experiment includes comprehensive test cases:

```python
# Test parentheses checker
test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
for expr in test_cases:
    result = checker.check(expr)
    print(f"'{expr}': {'✓' if result else '✗'}")
```

📚 Learning Outcomes

After completing this unit, you will be able to:

· ✅ Implement core linear data structures from scratch
· ✅ Analyze time and space complexity of operations
· ✅ Understand trade-offs between different implementations
· ✅ Apply data structures to solve real-world problems
· ✅ Write clean, modular, production-ready Python code

🤝 Contributing

Feel free to submit issues and enhancement requests!

📄 License

This project is for educational purposes as part of the Data Structures Lab Manual curriculum.

👨‍💻 Author

Data Structures Lab - Unit 2 Implementation

---

⭐ Star this repository if you found it helpful!
