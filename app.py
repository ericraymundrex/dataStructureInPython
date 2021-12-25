class Queue:
        def __init__(self):
                self.queue=[]
        def enqueue(self,data):
                self.queue.append(data)
        def dequeue(self):
                x=self.queue[0]
                self.queue.remove(self.queue[0])
                return x
        def is_empty(self):
                return len(self.queue)
class Node:
        def __init__(self,data=None,lnode=None,rnode=None):
                self.lnode=lnode
                self.data=data
                self.rnode=rnode
class Tree:
        def __init__(self):
                self.root=None
        def Create_a_tree(self):
                q=Queue()
                node=Node(input("Enter the data for the root node "))
                self.root=node
                q.enqueue(node)
                pointer=Node()
                while q.is_empty() != 0:
                        pointer=q.dequeue()
                        x=int(input(f"Enter the value of the left node of {pointer.data} "))
                        if(x!=-1):
                                temp=Node(x)
                                pointer.lnode=temp
                                q.enqueue(temp)
                        x=int(input(f"Enter the value of the left node of {pointer.data} "))
                        if(x!=-1):
                                temp=Node(x)
                                pointer.rnode=temp
                                q.enqueue(temp)
        def inorder(self,pointer):
                if pointer is not None:
                        print(pointer.data)
                        self.inorder(pointer.lnode)
                        self.inorder(pointer.rnode)

if __name__=="__main__":
        T= Tree()
        T.Create_a_tree()
        T.inorder(T.root)