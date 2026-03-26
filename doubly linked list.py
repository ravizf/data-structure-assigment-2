"""
Experiment 11: Doubly Linked List
Extended operations with bidirectional links
"""

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert_after_node(self, target_value, new_value):
        """Insert new node after node containing target_value - O(n) to find"""
        current = self.head
        while current and current.data != target_value:
            current = current.next
        
        if not current:
            print(f"Insert after {target_value}: Node not found")
            return False
        
        new_node = DNode(new_value)
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
        else:
            # Inserting after tail
            self.tail = new_node
        
        current.next = new_node
        self.length += 1
        print(f"Insert {new_value} after {target_value} → ", end="")
        self.display()
        return True
    
    def delete_at_position(self, position):
        """Delete node at given position (0-indexed)"""
        if position < 0 or position >= self.length:
            print(f"Delete at position {position}: Invalid position")
            return None
        
        # Case 1: Delete head
        if position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.length -= 1
            print(f"Delete at position {position} (head) → ", end="")
            self.display()
            return deleted_data
        
        # Case 2: Delete tail
        if position == self.length - 1:
            deleted_data = self.tail.data
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.length -= 1
            print(f"Delete at position {position} (tail) → ", end="")
            self.display()
            return deleted_data
        
        # Case 3: Delete middle
        current = self.head
        for _ in range(position):
            current = current.next
        
        deleted_data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self.length -= 1
        print(f"Delete at position {position} → ", end="")
        self.display()
        return deleted_data
    
    def display_forward(self):
        """Display list from head to tail"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Forward: {elements}, Length: {self.length}")
        return elements
    
    def display_backward(self):
        """Display list from tail to head (demonstrates bidirectional capability)"""
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        print(f"Backward: {elements}")
        return elements
    
    def display(self):
        self.display_forward()


# Test Experiment 11
print("="*50)
print("Experiment 11: Doubly Linked List")
print("="*50)

dll = DoublyLinkedList()

print("\n--- Building Initial List ---")
# Build initial list: 10 ↔ 20 ↔ 30 ↔ 40
for val in [10, 20, 30, 40]:
    dll.insert_after_node(dll.tail.data if dll.tail else None, val) if dll.head else dll.__setattr__('head', DNode(10)) or dll.__setattr__('tail', dll.head) or setattr(dll, 'length', 1) or print("Initialize with 10") or dll.display()
# Better approach - let's do it properly:
dll2 = DoublyLinkedList()
dll2.head = DNode(10)
dll2.tail = dll2.head
dll2.length = 1
print("\nInitial list:")
dll2.display()
dll2.insert_after_node(10, 20)
dll2.insert_after_node(20, 30)
dll2.insert_after_node(30, 40)
dll2.display()

print("\n--- Insert After Node ---")
dll2.insert_after_node(20, 25)   # Insert 25 after 20
dll2.insert_after_node(40, 45)   # Insert 45 after 40 (new tail)
dll2.insert_after_node(100, 50)  # Target not found

print("\n--- Delete at Position ---")
dll2.display_forward()
dll2.display_backward()  # Show backward traversal works
dll2.delete_at_position(0)    # Delete head (10)
dll2.delete_at_position(4)    # Delete tail (45)
dll2.delete_at_position(1)    # Delete middle (25)
dll2.delete_at_position(10)   # Invalid position

print("\n--- Complexity Summary ---")
print("| Operation | Time Complexity | DLL Advantage |")
print("|-----------|-----------------|----------------|")
print("| Insert after node | O(n) for search | O(1) for insertion once found |")
print("| Delete at position | O(n) to reach position | O(1) for pointer updates |")
print("| Delete given node | O(n) to find | O(1) with reference |")
print("| Backward traversal | O(n) | Unique to DLL |")
print("| Insert at beginning | O(1) | Update head and prev pointers |")
