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
#Three
class Three:
    def __init__(self):
        self.root=Node()
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

    def iterative_preorder_traversal(self):
        temp=self.root
        st=stack()
        st.insert(temp)
        while temp is not None or not(st.length_of_stack() ==0):
            if temp is not None:
                
                st.insert(temp)
                temp=temp.lchild
            else:
                temp=st.popdata()
                # print(temp.data)
                print(temp.data)
                temp=temp.rchild
        
if __name__=="__main__":
    t=Three()
    t.create_a_binary_three()
    t.iterative_preorder_traversal()
