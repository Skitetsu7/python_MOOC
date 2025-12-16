class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None) #For splay()

    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
            return

        self.splay(key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return

        n = Node(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if self.root is None or key != self.root.key:
            return

        # Now delete the root.
        if self.root.left== None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None

    def splay(self, key):
        l = r = self.header
        t = self.root
        if t is None:
            return
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t


def test():
    
    tree = SplayTree()
    tree.remove(123) #try to remove an element when the tree is empty to 
    #trigger lines 58-59 the in the remove function
    assert tree.isEmpty() #check that the tree is empty at the beginning, and at the end, no need to call it 
    #between as there is only one line to cover
    assert tree.findMin() is None #Check that the min and the Max don't exist, 
    #and that we can't find a number when the tree is empty. The three function are nearly the same, 
    #so we only need to call them when the tree is empty and when there are elements
    assert tree.findMax() is None
    assert tree.find(123) is None

    tree.insert(15)
    tree.insert(7)
    tree.insert(45)
    
    tree.remove(45)#we call the remove method to enter the else condition
    
    tree.insert(35)
    
    tree.remove(7)
    
    tree.insert(35)#we do this to go inside the insert function, as the element already exist
    tree.insert(-5)
    
    assert tree.findMax() == 35 #same as above for min and Max
    assert tree.findMin() == -5
    
    assert tree.find(35) == 35
    assert tree.find(5) is None
    

    
test()
