class Node:
    def __init__(self, val) -> None:
        self.key = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
        Implementation of AVL Tree 
    """
    def insert(self, root, val):

        # Step - 1: Perform the normal BST insertion
        if root == None:
            return Node(val)
        elif root.key > val:
            root.left = self.insert(root.left, val)
        elif root.key < val:
            root.right = self.insert(root.right, val)

        # Step - 2: Update the height of the ancestor node.
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step - 3: Get the balance factor
        balance = self.getBalanceFactor(root)

        # Step - 4: if the node is unbalanced trying out the four cases.

        # Case - 1: Left Left
        if balance > 1 and root.left.key > val:
            return self.rightRotate(root)
        
        # Case - 2: Right Right
        elif balance < -1 and root.right.key < val:
            return self.leftRotate(root)

        # Case - 3: Left Right
        elif balance > 1 and root.left.key < val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case - 4: Right Left
        elif balance < -1 and root.right.key > val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
    
        return root

    def leftRotate(self, root):
        """
        Rotate left if the tree is right skewed.

        Args:
            root (Node): Node of a tree

        Returns:
            Node: The new node after left rotation
        """
        y = root.right
        t2 = y.left

        # perform rotation
        y.left = root
        root.right = t2

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    
    def rightRotate(self, root):
        """
        Rotate right if the tree is left skewed.

        Args:
            root (Node): Node of a tree.

        Returns:
            Node: New node after the right rotation
        """
        y = root.left
        t3 = y.right

        # perform rotation
        y.right = root
        root.left = t3

        # update height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        """
        Get the height of a node.

        Args:
            root (Node): Node of a tree

        Returns:
            int: The height of the current node.
        """
        if root == None:
            return 0
        return root.height
    
    def getBalanceFactor(self, root):
        """
        Gets the balance factor of the node

        Args:
            root (Node): Node of a tree.

        Returns:
            int: Balance factor of the current node.
        """
        if root == None:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)


    # After this all the operations performed are similar to the BST operation. 

    def inorder(self, root):
        if root == None:
            return

        self.inorder(root.left)
        print(root.key, end = " ")
        self.inorder(root.right)

    def search(self, root, val):
        if root == None:
            return False
        elif root.key == val:
            return True
        elif root.key > val:
            return self.search(root.left, val)
        elif root.key < val:
            return self.search(root.right, val)
        

    def getRightMin(self, root):
        temp = root

        while temp.left != None:
            temp = temp.left
        
        return temp.key

    def delete(self, root, val):
        if root == None:
            return
        
        elif root.key > val:
            self.left = self.delete(root.left, val)
        
        elif root.key < val:
            self.right = self.delete(root.right, val)

        else:
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                rightMin = self.getRightMin(root.right)
                root.key = rightMin
                root.right = self.delete(root.right, rightMin)



if __name__ == "__main__":

    avl = AVLTree()
    root = None

    root = avl.insert(root, 10)
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)
    root = avl.insert(root, 40)
    root = avl.insert(root, 50)
    root = avl.insert(root, 25)


    print("Inorder Traversal")
    avl.inorder(root)
    print()
    avl.delete(root, 20)
    avl.inorder(root)
    print()