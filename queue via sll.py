"""
Experiment 13: Queue using Singly Linked List
O(1) operations with head and tail pointers
"""

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """Queue implementation using Singly Linked List with head & tail pointers"""
    
    def __init__(self):
        self.front = None   # Head - dequeue from here
        self.rear = None    # Tail - enqueue here
        self._size = 0
    
    def enqueue(self, data):
        """Add element to rear of queue - O(1)"""
        new_node = QueueNode(data)
        
        if not self.rear:
            # First element
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self._size += 1
        print(f"  Enqueue: {data} → Queue: ", end="")
        self.display()
    
    def dequeue(self):
        """Remove element from front of queue - O(1)"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        data = self.front.data
        self.front = self.front.next
        
        if not self.front:
            self.rear = None
        
        self._size -= 1
        print(f"  Dequeue: {data} → Queue: ", end="")
        self.display()
        return data
    
    def peek(self):
        """Get front element without removing - O(1)"""
        if self.is_empty():
            return None
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self._size
    
    def display(self):
        """Display queue from front to rear"""
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        print(f"[{' ← '.join(map(str, elements)) if elements else 'empty'}]")
        return elements


# Test Experiment 13
print("="*50)
print("Experiment 13: Queue via SLL")
print("="*50)

print("\n--- Part 1: Basic Queue Operations ---")
q = Queue()

print("\nEnqueue operations:")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print(f"\nFront element (peek): {q.peek()}")
print(f"Queue size: {q.size()}")

print("\nDequeue operations:")
q.dequeue()
q.dequeue()
q.dequeue()

print(f"\nAfter dequeues:")
print(f"Is empty? {q.is_empty()}")
q.display()

print("\nEnqueue more:")
q.enqueue(50)
q.enqueue(60)
q.display()

print("\n--- Part 2: BFS Simulation (Queue Application) ---")
print("\nSimulating BFS on a simple graph using queue:")

# BFS simulation
class SimpleGraph:
    def __init__(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }
    
    def bfs(self, start):
        """BFS traversal using queue"""
        queue = Queue()
        visited = set()
        traversal_order = []
        
        print(f"\nBFS starting from {start}:")
        print("-" * 40)
        
        queue.enqueue(start)
        visited.add(start)
        
        while not queue.is_empty():
            vertex = queue.dequeue()
            traversal_order.append(vertex)
            print(f"  Visiting: {vertex}")
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
                    print(f"    Adding {neighbor} to queue")
        
        print(f"\nBFS Traversal Order: {' → '.join(traversal_order)}")
        return traversal_order

graph = SimpleGraph()
graph.bfs('A')

print("\n--- Complexity Analysis ---")
print("="*50)
print("\n| Operation | Time Complexity | Explanation |")
print("|-----------|-----------------|-------------|")
print("| enqueue | O(1) | Insert at tail with rear pointer |")
print("| dequeue | O(1) | Remove from head with front pointer |")
print("| peek | O(1) | Direct access to front node |")
print("| isEmpty | O(1) | Check front pointer |")
print("| size | O(1) | Maintained count variable |")
print("\nQueue vs Array Implementation:")
print("| Aspect | Linked List Queue | Array Queue |")
print("|--------|------------------|-------------|")
print("| enqueue | O(1) always | O(1) amortized |")
print("| dequeue | O(1) always | O(n) if not circular |")
print("| Memory | Per node overhead | Contiguous, less overhead |")
print("| Growth | Unlimited | Requires resizing |")
print("\nWhy BFS uses Queue:")
print("- BFS explores level by level (FIFO)")
print("- First discovered nodes are processed first")
print("- Queue ensures vertices at distance d are processed before distance d+1")
print("- Guarantees shortest path in unweighted graphs")