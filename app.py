# iterative method for thaversal of the three

#Stack
class stack:
    def __init__(self):
        self.stack=[]
    def insert(self,data):
        self.stack.append(data)
    def popdata(self):
        x=self.stack[len(self.stack)-1]
        self.stack.remove(x)
        return x
    def length_of_stack(self):
        return len(self.stack)

# Queue
class Queue:
    def __init__(self):
        self.Queue=[]
    def enqueue(self,data):
        self.Queue.append(data)
    def dequeue(self):
        data=self.Queue[0]
        self.Queue.remove(data)
        return data
    def is_empty(self):
        return len(self.Queue)==0

# Node
class Node:
    def __init__(self,data=None,lchild=None,rchild=None):
        self.data,self.lchild,self.rchild=data,lchild,rchild

class BST:
        def __init__(self):
                self.root=Node()
                self.r_tail=Node()
        def create_a_binary_three(self):
                q=Queue()

                self.root=Node(int(input("Enter the data for the root node : ")))
                q.enqueue(self.root)

                while q.is_empty() is False:
                        parent=q.dequeue()
                        data=int(input(f"Enter the left child of {parent.data} : "))
                        if data !=-1:
                                temp=Node(data)
                                parent.lchild=temp
                                q.enqueue(parent.lchild)
                        data=int(input(f"Enter the right child of {parent.data} :"))
                        if data !=-1:
                                temp=Node(data)
                                parent.rchild=temp
                                q.enqueue(parent.rchild)
        
                print("The binary tree is created")

        def search(self,key):
                # print(self.root.data)
                itr=self.root
                while itr is not None:
                        print(itr.data)
                        if itr.data == key:
                                return True
                        elif itr.data>key:
                                itr=itr.lchild
                        else:
                                itr=itr.rchild
                return False
        def insert(self,data):
                if self.root.data is None:
                        self.root.data=data
                        return None

                itr=self.root
                while itr is not None:
                        tail=itr
                        if itr.data==data:
                                return "The data is already there"
                        elif itr.data>data:
                                itr=itr.lchild
                        else:
                                itr=itr.rchild
                temp=Node(data)
                if data<tail.data:
                        tail.lchild=temp
                else:
                        tail.rchild=temp
                print("-")
        def insert_recursive(self,itr,data):
                if self.root.data is None:
                        self.root=Node(data)
                        return None
                if itr is not None:
                        self.r_tail=itr
                        if itr.data==data:
                                return False
                        elif itr.data>data:
                                self.insert_recursive(itr.lchild,data)
                        else:
                                self.insert_recursive(itr.rchild,data)
                else:
                        if data<self.r_tail.data:
                                self.r_tail.lchild=Node(data)
                        else:
                                self.r_tail.rchild=Node(data)
        def create_from_list(self,li):
                print(li)
                for x in li:
                        self.insert_recursive(self.root,x)
        def inorder(self,itr):
                if itr is not None:
                        self.inorder(itr.lchild)
                        print(itr.data)
                        self.inorder(itr.rchild)

if __name__=="__main__":
        t=BST()
        li=[10,30,40,20,50,50]
        t.create_from_list(li)
        t.inorder(t.root)