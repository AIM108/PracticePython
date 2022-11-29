import random as r
import string
class node(object):
    def __init__(self,d,l,r,n):
        self.name=n
        self.data =d
        self.left =l
        self.right =r
    def printNode(self):
        print("Data: ",self.data)
        print("Name: ",self.name)
    def getLeftNode(self):
        return self.left
    def getRightNode(self):
        return self.right
    def getData(self):
        return self.data
    def getName(self):
        return self.name


def generateBianaryGraph(height):
    data = r.random()
    name = r.choices(string.ascii_uppercase, k=1)
    if height == 0:
        leaf = node(data,None,None,name)
        return leaf
    else:
        left = generateBianaryGraph(height -1)
        right =generateBianaryGraph(height-1)
        root = node(data,left,right,name)
        return root


def printLargerPath(Tree):
    if (Tree.getLeftNode() == None) and (Tree.getRightNode() == None):
        return "End"
    else:
        left =Tree.getLeftNode()
        right =Tree.getRightNode()
        if left.getData() >= right.getData():
            print(left.getName() ,left.getData())
            printLargerPath(left)
        else:
            print(right.getName(), right.getData())
            printLargerPath(right)
        


def main():
    tree =generateBianaryGraph(10)
    printLargerPath(tree)


    print("End of program")




if __name__ =="__main__":
    main()