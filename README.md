# Binary Search Tree
Binary tree is a Data Structure in which each node can have atmost 2 children.
A Binary Tree in which for each node, value of all the nodes in the left subtree is lesser or equal and value of all the nodes in the right subtree is greater.(Must be true for all nodes). In an array the starting value is always the root node. 
 

![image](https://user-images.githubusercontent.com/72907502/122736484-b6974f00-d29d-11eb-9394-631fc7be8db2.png)

## Applications
1. Efficient structure to organize data for quick search and update.
2. It is used to implement multilevel indexing in DATABASE.


## Binary Tree Traversal
Refers to the process of visiting each node in the Tree Data Structure, exactly once. We always start with the root (head) node. We cannot randomly access any node in the tree. There are three ways to traverse a tree
1. In-order Traversal: In this, the left subtree is visited first, then the root value and after that the right subtree is visited. We should always remember that every node may represent a subtree itself.
2. Pre-Order Traversal: In this, the root value is visited first, then the left subtree and finally the right subtree is visited.
3. Post-Order Traversal: In this, the left subtree is visited first, then the right subtree and then finally the root value is printed.
