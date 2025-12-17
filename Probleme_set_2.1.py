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


import probleme_set
from probleme_set_2 import SplayTree


def test():
    #Your code here
    st = SplayTree() #cover _init_
    
    #fisrt step: empty tree
    assert st.findMin() is None #cover "if root == None" in findMin
    assert st.findMax() is None #cover "if root == None" in findMax
    assert st.find(157) is None #cover "if root == None" in find
    st.remove(20) #cover "if root is None" in remove

    #second step: insertions
    st.insert(20)  #cover "if root == None" in insert
    st.insert(20) #cover "if root.key == key" (doublon par rapport à celui au dessus)
    st.insert(25) #pass by "else key>root.key"

    #third step: forced splay
    st.splay(28)
    st.insert(15) #pass by "if key<roor.key"

    #fourth step: verify min/max
    assert st.findMin() == 15
    assert st.findMax() == 25
    
    #fifth step: verify find
    assert st.find(15) == 15 #cover "return root.key"
    assert st.find(5) is None #cover "if root.key != key"

    #sixth step: verify remove
    st.remove(20) #cover "else"
    st.remove(15) #cover "if root.left ==None"
    assert st.isEmpty() is False #cover isEmpty
    
    #seventh step: called multiple times splay()
    st.insert(24)
    st.insert(23)
    st.insert(46)
    st.insert(18)
    st.insert(2)
    st.insert(76)
    st.insert(7)
