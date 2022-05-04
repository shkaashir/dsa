class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None
        self.parent = None

class BST:
    
    def insert(self, root=None, val=None):
        """
        Insert the given value in a tree.

        Args:
            root (Node): Root Node of a tree. Defaults to None
            val: Val to be added in a tree. Defaults to None.
        """

        if root == None:
            # It is the root node of a tree
            return Node(val)
        elif root.key > val:
            # If node key is greater than value insert in left sub tree.
            root.left = self.insert(root.left, val)
            root.left.parent = root
        elif root.key < val:
            # else node key is lower than value insert in right sub tree. 
            root.right = self.insert(root.right, val)
            root.right.parent = root
        return root


    def inorder(self, root):
        """
        Traverse the tree in following order.
            Left --> Root --> Right

        Args:
            root (Node): The root node of a tree.
        """
        if root == None:
            return

        self.inorder(root.left)
        print(root.key, end=" ")
        self.inorder(root.right)

    def search(self, root, val):
        """

        Search the given value in a tree.

        Args:
            root (Node): Root node of a tree.
            val: Value to be searched in a tree.

        Returns:
            boolean: Returns true if value found in tree else false
        """
        if root == None:
            # If value is not found and has reached the end of the tree
            return False
        elif root.key == val:
            # else if value is found in the tree
            return True
        elif root.key > val:
            # else if node key is greater than value to be searched then search in left sub tree.
            return self.search(root.left, val)
        elif root.key < val:
            # else if node key is lower than value to be searched then search in right sub tree.
            return self.search(root.right, val)
    
    def getRightMax(self, root):
        
        temp = root

        while temp.left != None:
            temp = temp.left
        
        return temp.key

    def delete(self, root, val):
        """
        Delete the value in a tree.

        Args:
            root (Node): Root node of a tree.
            val: Value to be deleted in a tree.
        """
        if root == None:
            return
        elif root.key > val:
            root.left = self.delete(root.left, val)
        elif root.key < val:
            root.right = self.delete(root.right, val)
        else:
             # Case 1: If the node has no any child.
            if root.left == None and root.right == None:
                return None

            # Case 2: If the node has only one child.
            elif root.left == None:
                # it has only right child
                return root.right
            elif root.right == None:
                # it has only left child 
                return root.left
            
            # Case 3: If the node has two children.
            else:
                # get the node which is right next in line of inorder traversal.
                rightMin = self.getRightMax(root.right)
                root.key = rightMin
                root.right = self.delete(root.right, rightMin)

    def getParent(self, root, val):
        """
        Get parent of the given value.

        Args:
            root (Node): Root node of a tree.
            val: Value of which the parent is to be found

        Returns:
            _type_: _description_
        """
        if root == None:
            return "Value not found."
        
        elif root.key == val:
            return root.parent.key
        
        elif root.key > val:
            return self.getParent(root.left, val)
        
        elif root.key < val:
            return self.getParent(root.right, val)

if __name__ == "__main__":

    bst = BST()

    root = bst.insert(val=100)
    root = bst.insert(root, 50)
    root = bst.insert(root, 150)
    root = bst.insert(root, 250)

    bst.inorder(root)
    print()
    
    print(bst.getParent(root, 250))

