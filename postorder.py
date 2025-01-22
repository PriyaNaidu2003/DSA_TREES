class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class postorderTraversel:
    def postorder(self, root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
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
nodes=[1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
tree=BuildTree()
root=tree.build(nodes)
traverse=postorderTraversel()
print(traverse.postorder(root))