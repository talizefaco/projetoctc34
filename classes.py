

class TreeNode:
    def __init__(self,value="",left=None,right=None,parent=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        
    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def getParent(self):
        return self.parent

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def setLeftChild(self, leftChild):
        leftChild.parent = self
        self.leftChild = leftChild
        return self.leftChild

    def setRightChild(self, rightChild):
        rightChild.parent = self
        self.rightChild = rightChild
        return self.rightChild

    def createLeftChild(self):
        self.leftChild = TreeNode("", None, None, self)
        return self.leftChild

    def createRightChild(self):
        self.rightChild = TreeNode("", None, None, self)
        return self.rightChild

    def printValue(self):
        print(self.value)

    def traverse(self):
        thislevel = [self]
        middle = "       "
        blankspaces = ""
        a = '                                  '
        print(a + str(self.value))
        i = 3

        while thislevel:
            nextlevel = []
            printlevel = []
            length = len(a) - i
            a = a[:length]
            printlevel.append(a)
            middle = middle[:len(middle) - 1]

            for n in thislevel:
                if n.hasBothChildren():
                    children = str(n.leftChild.value)
                    children = children + middle
                    children = children + str(n.rightChild.value)
                    children = children + "  "
                    printlevel.append(children)
                    
                    nextlevel.append(n.leftChild)
                    nextlevel.append(n.rightChild)

                elif n.hasLeftChild():
                    children = str(n.leftChild.value)
                    children = children + "       "
                    printlevel.append(children)
                    
                    nextlevel.append(n.leftChild)

                elif n.hasRightChild():
                    children = "     "
                    children = str(n.rightChild.value)
                    children = children + "  "
                    printlevel.append(children)
                    
                    nextlevel.append(n.leftChild)

                else:
                    blankspaces = blankspaces + "       "
                    # printlevel.append("      ")

            printlevel.insert(0, blankspaces)
            # print(len(blankspaces),end="")
            # print("--",end="")
            # print(len(a),end="")
            for m in printlevel:
                print(m, end="")
            print("")
            
            thislevel = nextlevel
            i = i + 2

class Tree:
    def __init__(self):
        self.root = TreeNode()
    
    def getRoot(self):
        return self.root

    def tela(self):
        self.root.traverse()


class Pilha:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

