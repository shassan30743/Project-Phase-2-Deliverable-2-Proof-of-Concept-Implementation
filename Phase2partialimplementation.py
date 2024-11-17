class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.data:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if not node or node.data == value:
            return node
        if value < node.data:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node
        
        if value < node.data:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.data:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children: Get the inorder successor
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_recursive(node.right, temp.data)
        
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


# Initialize the BST
bst = BinarySearchTree()

# Test Insertions
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)
print("In-order Traversal after insertion:", bst.inorder_traversal())

# Test Search
print("Search for 4:", "Found" if bst.search(4) else "Not Found")
print("Search for 10:", "Found" if bst.search(10) else "Not Found")

# Test Deletion
bst.delete(3)
print("In-order Traversal after deleting 3:", bst.inorder_traversal())

bst.delete(7)
print("In-order Traversal after deleting 7:", bst.inorder_traversal())

# Test Deleting the Root
bst.delete(5)
print("In-order Traversal after deleting root (5):", bst.inorder_traversal())
