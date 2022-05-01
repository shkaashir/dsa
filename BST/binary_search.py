class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None

class BST:
    def insert(self, root=None, val=None):
        """_summary_

        Args:
            root (Node): Root Node of a tree. Defaults to None
            val (str): Val to be added in a tree. Defaults to None.
        """

        if root == None:
            return Node(val)
        elif root.key > val:
            root.left = self.insert(root.left, val)
        elif root.key < val:
            root.right = self.insert(root.right, val)
        
        return root


    def inorder(self, root):
        """
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
        if root == None:
            return False
        elif root.key == val:
            return True
        elif root.key > val:
            return self.search(root.left, val)
        elif root.key < val:
            return self.search(root.right, val)
    
    def getRightMax(self, root):
        
        temp = root

        while temp.left != None:
            temp = temp.left
        
        return temp.key

    def delete(self, root, val):
        if root == None:
            return
        elif root.key > val:
            root.left = self.delete(root.left, val)
        elif root.key < val:
            root.right = self.delete(root.right, val)
        else:
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                rightMin = self.getRightMax(root.right)
                root.key = rightMin
                root.right = self.delete(root.right, rightMin) 
        
        





if __name__ == "__main__":

    bst = BST()

    root = bst.insert(val=100)
    root = bst.insert(root, 50)
    root = bst.insert(root, 150)

    bst.inorder(root)
    
    print()

    print(bst.search(root, 510))

    print()
