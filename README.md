# Data Structures & Algorithms in Python

A comprehensive collection of fundamental data structures and algorithms implemented in Python. This repository serves as a learning resource and reference for common computer science concepts.

## Table of Contents

- [Overview](#overview)
- [Data Structures](#data-structures)
- [Algorithms](#algorithms)
- [File Descriptions](#file-descriptions)
- [Requirements](#requirements)
- [Usage](#usage)

## Overview

This repository contains Python implementations of essential data structures and algorithms, including arrays, linked lists, hash tables, trees, and various search and traversal algorithms. Each implementation is designed to be clear, educational, and easy to understand.

## Data Structures

### Arrays
- **File**: [arrays.py](arrays.py)
- Basic array operations including indexing, modification, iteration, and appending elements
- Demonstrates fundamental Python list operations

### Hash Tables
- **File**: [HashTable.py](HashTable.py)
- Dictionary implementation with O(1) average lookup time
- Includes both hash map (dictionary) and hash set implementations
- Demonstrates key-value storage and membership testing

### Linked Lists
- **File**: [LinkedList.py](LinkedList.py)
- Singly linked list implementation with custom Node class
- Operations: traversal and insertion at specific positions
- Time complexity: O(n) for traversal and insertion

### Binary Search Trees
- **File**: [trees.py](trees.py)
- Binary Search Tree (BST) implementation
- Operations: insert, delete, and find minimum value
- Maintains BST property where left children < parent < right children

## Algorithms

### Binary Search
- **File**: [binarySearch.py](binarySearch.py)
- Efficient search algorithm for sorted arrays
- Time complexity: O(log n)
- Returns boolean indicating whether target exists in array
- Uses floor and ceiling index approach

### Breadth-First Search (BFS)
- **File**: [BFS.py](BFS.py)
- Graph traversal algorithm that explores nodes level by level
- Uses queue data structure (deque) for efficient operations
- Time complexity: O(V + E) where V is vertices and E is edges
- Returns nodes in BFS order

### Depth-First Search (DFS)
- **File**: [DFS.py](DFS.py)
- Tree traversal algorithms using recursion
- Three traversal methods implemented:
  - **Preorder**: Root → Left → Right
  - **Inorder**: Left → Root → Right
  - **Postorder**: Left → Right → Root
- Time complexity: O(n) where n is number of nodes

## File Descriptions

### [arrays.py](arrays.py)
Basic array operations demonstration:
- Accessing elements by index
- Modifying array elements
- Getting array length
- Iterating through arrays
- Appending new elements

**Example output**: Prints individual grades and the modified grades list.

---

### [HashTable.py](HashTable.py)
Hash-based data structures:
- **Dictionary (Hash Map)**: Stores student names as keys and grades as values
- **Set (Hash Set)**: Stores unique student names
- Demonstrates O(1) lookup operations
- Shows membership testing with `in` operator

**Example output**: Individual student grades and membership test results.

---

### [LinkedList.py](LinkedList.py)
Singly linked list implementation:
- `Node` class: Represents individual list nodes with data and next pointer
- `traversingALinkedList(head)`: Traverses and prints the entire linked list
- `insertAtNode(head, newNode, position)`: Inserts a node at specified position

**Example usage**: Creates a linked list (7→4→1→3), inserts 100 at position 2, resulting in (7→100→4→1→3).

---

### [binarySearch.py](binarySearch.py)
Binary search algorithm implementation:
- `binary_search(target, nums)`: Searches for target in sorted array
- Uses floor and ceiling indices to narrow search space
- Halves search space in each iteration
- Returns `True` if found, `False` otherwise

**Use case**: Efficient searching in sorted arrays with O(log n) complexity.

---

### [BFS.py](BFS.py)
Breadth-first search for graphs:
- `bfs(graph, start)`: Traverses graph level by level from start node
- Uses `deque` for efficient queue operations
- Tracks visited nodes to avoid cycles
- Returns list of nodes in BFS traversal order

**Example**: Graph with 10 nodes, starting from node 1.

**Output**: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` (BFS order)

---

### [DFS.py](DFS.py)
Depth-first search tree traversal:
- `TreeNode` class: Binary tree node with value, left, and right children
- `preorder(root)`: Visits root, then left subtree, then right subtree
- `inorder(root)`: Visits left subtree, root, then right subtree
- `postorder(root)`: Visits left subtree, right subtree, then root

**Example tree structure**:
```
       1
      / \
     2   3
    / \   \
   4   5   6
```

**Traversal outputs**:
- Preorder: `1 2 4 5 3 6`
- Inorder: `4 2 5 1 3 6`
- Postorder: `4 5 2 6 3 1`

---

### [trees.py](trees.py)
Binary Search Tree implementation:
- `TreeNode` class: BST node with value, left, and right children
- `insert(root, value)`: Inserts value maintaining BST property
- `delete(root, value)`: Removes node with three cases:
  - Leaf node: Simply remove
  - One child: Replace with child
  - Two children: Replace with inorder successor
- `find_min(node)`: Finds minimum value in subtree

**BST Property**: For any node, all left descendants < node < all right descendants.

## Requirements

- Python 3.x
- No external dependencies (uses only Python standard library)

## Usage

Each file can be run independently to see the implementation in action:

```bash
# Run binary search example
python binarySearch.py

# Run BFS traversal
python BFS.py

# Run DFS traversals
python DFS.py

# Run linked list operations
python LinkedList.py

# Run array operations
python arrays.py

# Run hash table examples
python HashTable.py

# Tree operations (trees.py defines functions but doesn't execute them)
python trees.py
```

## Time Complexity Summary

| Operation | Data Structure | Time Complexity |
|-----------|---------------|-----------------|
| Array Access | Array | O(1) |
| Hash Table Lookup | Dictionary/Set | O(1) average, O(n) worst |
| Linked List Traversal | Linked List | O(n) |
| Linked List Insertion | Linked List | O(n) |
| Binary Search | Sorted Array | O(log n) |
| BFS Traversal | Graph | O(V + E) |
| DFS Traversal | Tree | O(n) |
| BST Insert | Binary Search Tree | O(log n) average, O(n) worst |
| BST Delete | Binary Search Tree | O(log n) average, O(n) worst |

## Learning Path

For beginners, recommended order of study:

1. [arrays.py](arrays.py) - Start with basic arrays
2. [HashTable.py](HashTable.py) - Learn hash-based structures
3. [LinkedList.py](LinkedList.py) - Understand linked data structures
4. [binarySearch.py](binarySearch.py) - Learn efficient searching
5. [trees.py](trees.py) - Binary search trees
6. [DFS.py](DFS.py) - Tree traversal techniques
7. [BFS.py](BFS.py) - Graph traversal techniques

## Contributing

Feel free to add more data structures and algorithms to this collection. Ensure code is well-commented and follows Python best practices.

## License

This project is open source and available for educational purposes.
