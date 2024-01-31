class Node:
    def __init__(self, left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, item):
        n = Node(None, item, None)
        if self.root is None:
            self.root = n
            return
        # self.insert_rec(self.root, n, item)
        temp = self.root
        while True:
            if temp.item == item:
                print("Cannot insert duplicate values")
                break
            if temp.item < item:
                if temp.right is None:
                    temp.right = n
                    break
                else:
                    temp = temp.right

            if temp.item > item:
                if temp.left is None:
                    temp.left = n
                    break
                else:
                    temp = temp.left

    def insert_rec(self, root, n, item):
        if root is None or root.item == item:
            return
        if root.item < item:
            if root.right is None:
                root.right = n
            else:
                self.insert_rec(root.right, n, item)
        else:
            if root.left is None:
                root.left = n
            else:
                self.insert_rec(root.left, n, item)

    def search(self, item):
        # return self.search_rec(self.root, item)
        temp = self.root
        while temp is not None:
            if temp.item == item:
                return temp
            elif temp.item > item:
                temp = temp.left
            else:
                temp = temp.right

    def search_rec(self, root, item):
        if root is None or root.item == item:
            return root

        if root.item > item:
            return self.search_rec(root.left, item)
        else:
            return self.search_rec(root.right, item)

    def preorder(self):
        # self.preorder_rec(self.root)
        stack = [self.root]
        temp = self.root
        while len(stack) > 0:
            while temp is not None:
                stack.append(temp)
                temp = temp.left
            temp = stack.pop()
            while temp is not None:
                print(temp.item)
                if temp.right is not None:
                    temp = temp.right
                    break
                temp = stack.pop()

    def preorder_rec(self, root):
        if root is None:
            return
        print(root.item)
        self.preorder_rec(root.left)
        self.preorder_rec(root.right)

    def inorder(self):
        # self.inorder_rec(self.root)
        temp = self.root
        stack = [None]
        while temp is not None:
            while temp is not None:
                stack.append(temp)
                temp = temp.left

            temp = stack.pop()
            while temp is not None:
                print(temp.item)
                if temp.right is not None:
                    temp = temp.right
                    break
                temp = stack.pop()

    def inorder_rec(self, root):
        if root is None:
            return
        self.inorder_rec(root.left)
        print(root.item)
        self.inorder_rec(root.right)

    def postorder(self):
        self.postorder_rec(self.root)

    def postorder_rec(self, root):
        if root is None:
            return
        self.postorder_rec(root.left)
        self.postorder_rec(root.right)
        print(root.item)

    def min_value(self, root):
        temp = root
        while temp.left is not None:
            temp = temp.left
        return temp.item

    def max_value(self, root):
        temp = root
        while temp.right is not None:
            temp = temp.right
        return temp.item

    def delete(self, item):
        # par = None
        # child = self.root
        # while child is not None:
        #     if child.item == item:
        #         break
        #     par = child
        #     if child.item > item:
        #         child = child.left
        #     else:
        #         child = child.right
        # if child is None:
        #     print("Item not found")
        #     return
        #
        # # Two Children
        # if child.left is not None and child.right is not None:
        #     par = child
        #     predecessor = child.left
        #     while predecessor.right is not None:
        #         par = predecessor
        #         predecessor = predecessor.right
        #     child.item = predecessor.item
        #     child = predecessor
        #
        # # No Child
        # if child.left is None and child.right is None:
        #     if par is None:
        #         self.root = None
        #     elif par.item < child.item:
        #         par.right = None
        #     else:
        #         par.left = None
        # # One Child
        # elif child.left is None and child.right is not None:
        #     if par is None:
        #         self.root = child.right
        #     elif par.item < child.item:
        #         par.right = child.right
        #     else:
        #         par.left = child.right
        # elif child.left is not None and child.right is None:
        #     if par is None:
        #         self.root = child.left
        #     elif par.item < child.item:
        #         par.right = child.left
        #     else:
        #         par.left = child.left
        self.delete_rec(self.root, item)

    def delete_rec(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.delete_rec(root.left, data)
        elif data > root.item:
            root.right = self.delete_rec(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            self.delete_rec(root.right, root.item)
        return root

    def size(self):
        return self.size_rec(self.root)

    def size_rec(self, root):
        if root is None:
            return 0
        count = 1
        count += self.size_rec(root.left)
        count += self.size_rec(root.right)
        return count


# bst = BST()
# bst.insert(70)
# bst.insert(10)
# bst.insert(25)
# bst.insert(90)
# bst.insert(60)
# bst.insert(40)
# bst.insert(100)
# bst.insert(45)
#
# bst.preorder()
# bst.inorder()
# bst.postorder()

# bst = BST()
# bst.insert(50)
# bst.insert(30)
# bst.insert(80)
# bst.insert(10)
# bst.insert(40)
# bst.insert(70)
# bst.insert(100)
bst = BST()
bst.insert(20)
bst.insert(10)
bst.insert(30)
bst.insert(8)
bst.insert(12)
bst.insert(28)
bst.insert(35)
bst.insert(9)
bst.insert(27)

bst.inorder()
print()

bst.delete(20)
# bst.preorder_rec(bst.root)
# print()
# bst.preorder()

# bst.inorder_rec(bst.root)
# print()
bst.inorder()
print()
# bst.postorder()

print('Size of bst is', bst.size())
print('Min element of bst is', bst.min_value(bst.root))
print('Max element of bst is', bst.max_value(bst.root))
# print(bst.search(110) is None)
# print(bst.search(80) is None)
