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
        y = root.right
        t2 = y.left

        # perform rotation
        y.left = root
        root.right = t2

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    
    def rightRotate(self, root):
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
        if root == None:
            return 0
        return root.height
    
    def getBalanceFactor(self, root):
        if root == None:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)

    def inorder(self, root):
        if root == None:
            return

        self.inorder(root.left)
        print(root.key, end = " ")
        self.inorder(root.right)


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