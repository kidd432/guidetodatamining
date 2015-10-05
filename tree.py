__author__ = 'nake12'
class node:
    def __init__(self,value):
        self.left = None
        self.value = value;
        self.right = None

class Tree:
    def createTree(self,value):
        return node(value)

    def insertNode(self,node,value):
        if node is None:
            return self.createTree(value)
        if value <node.value:
            node.left = self.insertNode(node.left,value)
        if value >node.value:
            node.right = self.insertNode(node.right,value)

        return node
    def searchNode(self,node,value):
        if node is None or node.value == value:
            return node
        if value<node.value:
            return self.searchNode(node.right,value)
        if value > node.value:
            return self.searchNode(node.left,value)

    def deleteNode(self,node,value):
        if node is None:
            return None

        if value<node.value:
            node.left = self.deleteNode(node.left,value)
        elif value>node.value:
            node.right = self.deleteNode(node.right,value)
        else:
            if node.left is None and node.right is None:
                del node
            if node.left is None:
                temp = node.right
                del node
                return temp
            if node.right is None:
                temp = node.left
                del node
                return temp
        return node

    def traverseInorder(self,root):
        if root is not None:
            self.traverseInorder(root.left)
            print(root.value)
            self.traverseInorder(root.right)

    def traversePreorder(self,root):
        if root is not None:
            print(root.value)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self,root):
        if root is not None:
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            print(root.value)

def main():
    root = None
    tree = Tree()
    root = tree.insertNode(root, 10)
    print(root)
    tree.insertNode(root, 20)
    tree.insertNode(root, 30)
    tree.insertNode(root, 40)
    tree.insertNode(root, 70)
    tree.insertNode(root, 60)
    tree.insertNode(root, 80)

    print("Traverse Inorder:")
    tree.traverseInorder(root)

    print ("Traverse Preorder:")
    tree.traversePreorder(root)

    print ("Traverse Postorder:")
    tree.traversePostorder(root)


if __name__ == "__main__":
    main()