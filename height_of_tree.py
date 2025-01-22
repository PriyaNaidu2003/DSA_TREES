class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BuildTree:
    def __init__(self):
        self.indx=-1
    def build(self,nodes):
        self.indx+=1
        if nodes[self.indx]==-1:
            return None
        node=Node(nodes[self.indx])
        node.left=self.build(nodes)
        node.right=self.build(nodes)
        return node
    def heightoftree(self,root):
        if root==None:
            return 0
        leftheight=self.heightoftree(root.left)
        rightheight=self.heightoftree(root.right)
        maxheight=max(leftheight,rightheight)+1
        return maxheight

nodes=[1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,8,-1,-1]
tree=BuildTree()
root=tree.build(nodes)
print(tree.heightoftree(root))
