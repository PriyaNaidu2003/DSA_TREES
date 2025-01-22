class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Queue:

    def __init__(self,root):
        self.front=0
        self.rear=0
        self.q = [root,None]

    def push(self,data):
        self.q.append(data)
        self.rear+=1
    def pop(self):
        curr=self.q[self.front]
        self.front+=1
        return curr
    def display(self):
        print(q[front])
    def isEmpty(self):
        return len(self.q)




class levelorderTraversel:
    def levelorder(self, root):
        if root==None:
            return
        qu=Queue(root)
        while qu.isEmpty():

            curr=qu.pop()

            if curr is None:


                if not qu.isEmpty():
                    break

                qu.push(None)


            else:
                print(curr.data,end=" ")
                if curr.left!=None:
                    qu.push(curr.left)
                if curr.right!=None:
                    qu.push(curr.right)


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
traverse=levelorderTraversel()
traverse.levelorder(root)