"""
Experiment 12: Stack using Singly Linked List
With Balanced Parentheses Checker Application
"""

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """Stack implementation using Singly Linked List (head as top)"""
    
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, data):
        """Push element onto stack - O(1)"""
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        print(f"  Push: {data}")
    
    def pop(self):
        """Pop element from stack - O(1)"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        self._size -= 1
        print(f"  Pop: {data}")
        return data
    
    def peek(self):
        """Peek at top element - O(1)"""
        if self.is_empty():
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size
    
    def display(self):
        """Display stack from top to bottom"""
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Stack (top → bottom): {elements}")
        return elements


class ParenthesesChecker:
    """Application: Check balanced parentheses using Stack"""
    
    def __init__(self):
        self.stack = Stack()
        self.pairs = {')': '(', ']': '[', '}': '{'}
        self.open_brackets = set('([{')
        self.close_brackets = set(')]}')
    
    def check(self, expression):
        """Check if parentheses in expression are balanced"""
        print(f"\nChecking: '{expression}'")
        print("-" * 40)
        
        for i, char in enumerate(expression):
            if char in self.open_brackets:
                self.stack.push(char)
                print(f"  Position {i}: Opening '{char}' → push")
            
            elif char in self.close_brackets:
                if self.stack.is_empty():
                    print(f"  ❌ Position {i}: Closing '{char}' with no matching opening bracket")
                    return False
                
                top = self.stack.pop()
                expected_open = self.pairs[char]
                
                if top != expected_open:
                    print(f"  ❌ Position {i}: '{char}' doesn't match top '{top}'")
                    return False
                else:
                    print(f"  Position {i}: Closing '{char}' matches '{top}' → pop")
        
        # After processing all characters
        if self.stack.is_empty():
            print(f"  ✓ All brackets matched correctly")
            return True
        else:
            remaining = self.stack.display()
            print(f"  ❌ Unmatched opening brackets: {remaining}")
            return False


# Test Experiment 12
print("="*50)
print("Experiment 12: Stack via SLL + Parentheses Checker")
print("="*50)

print("\n--- Part 1: Stack Operations ---")
stack = Stack()
print("\nPushing elements:")
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print(f"\nPeek: {stack.peek()}")
print(f"Pop: {stack.pop()}")
print(f"Pop: {stack.pop()}")
stack.display()
print(f"Is empty? {stack.is_empty()}")
print(f"Pop: {stack.pop()}")
print(f"Is empty? {stack.is_empty()}")

print("\n--- Part 2: Balanced Parentheses Checker ---")
checker = ParenthesesChecker()

test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "((()))",
    "(()",
    "",
    "{[()]}()",
]

print("\n--- Test Results Summary ---")
print("="*50)
for expr in test_cases:
    result = checker.check(expr)
    status = "✓ BALANCED" if result else "✗ UNBALANCED"
    print(f"\nResult: {status}")
    print("="*50)

print("\n--- Complexity Analysis ---")
print("| Operation | Time Complexity | Space Complexity |")
print("|-----------|-----------------|------------------|")
print("| push | O(1) | O(1) per node |")
print("| pop | O(1) | O(1) |")
print("| peek | O(1) | O(1) |")
print("| Parentheses Check | O(n) | O(n) worst case |")
print("\nWhy Stack is ideal for parentheses checking:")
print("- LIFO property matches nesting behavior")
print("- Most recent opening bracket must match next closing bracket")
print("- Handles nested structures naturally")