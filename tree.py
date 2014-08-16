
class Tree:
    def __init__(self, root):
        self.root = root


    def get_root(self):
        return self.root


    def insert(self, node):
        self.root.insert(node, self.root)


    def delete(self, x):
        node = self.contains(x, self.root)
        self.root.delete(node)


    def preorder_traverse(self, node):
        if node:
            print node.val  # preorder
            self.preorder_traverse(node.left_child)
            self.preorder_traverse(node.right_child)


    def inorder_traverse(self, node):
        if node:
            self.inorder_traverse(node.left_child)
            print node.val  # inorder
            self.inorder_traverse(node.right_child)


    def postorder_traverse(self, node):
        if node:
            self.postorder_traverse(node.left_child)
            self.postorder_traverse(node.right_child)
            print node.val  # postorder


    def contains(self, x, node):
        if not node:
            return False
        elif x == node.val:
            return True
        elif x < node.val:
            return self.contains(x, node.left_child)
        else:
            return self.contains(x, node.right_child)


    def find_min(self, node):
        if not node.left_child:
            return node
        else:
            return self.find_min(node.left_child)


    def find_max(self, node):
        if not node.right_child:
            return node
        else:
            return self.find_max(node.right_child)


    def find_smaller(self, x, node):
        if not node:
            return False

        elif node.val >= x:
            self.find_smaller(x, node.left_child)

        elif node.val < x:
            print node.val
            self.find_smaller(x, node.left_child)
            self.find_smaller(x, node.right_child)

